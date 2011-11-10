from django import template
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.importlib import import_module
from django.utils.safestring import mark_safe


register = template.Library()


def load_callable(path_to_callable):
    try:
        mod_name, func_name = path_to_callable.rsplit(".", 1)
    except ValueError:
        raise Exception("Improperly configured.")
    try:
        mod = import_module(mod_name)
    except ImportError:
        raise Exception("Could not import %s" % mod_name)
    try:
        func = getattr(mod, func_name)
    except AttributeError:
        raise Exception("The module '%s' does not contain '%s'." % (mod_name, func_name))
    return func


class RemindersNode(template.Node):
    
    @classmethod
    def handle_token(cls, parser, token):
        bits = token.split_contents()
        if len(bits) != 3:
            raise template.TemplateSyntaxError
        return cls(as_var = bits[2])
    
    def __init__(self, as_var):
        self.as_var = as_var
    
    def render(self, context):
        request = context["request"]
        reminders = []
        for label in settings.REMINDERS:
            if label not in request.session:
                test = settings.REMINDERS[label]["test"]
                message = settings.REMINDERS[label]["message"]
                if not callable(test):
                    test = load_callable(test)
                url = None
                if settings.REMINDERS[label].get("dismissable", True):
                    url = reverse("reminders_dismiss", kwargs={"label": label})
                reminders.append({
                    "message": mark_safe(message % test(request.user)),
                    "dismiss_url": url
                })
        context[self.as_var] = reminders
        return ""


@register.tag
def reminders(parser, token):
    """
    Usage::
        {% reminders as var %}
    
    Returns a list of reminders
    """
    return RemindersNode.handle_token(parser, token)
