from django.conf import settings
from django.http import HttpResponse, Http404, HttpResponseNotAllowed

from reminders.models import Dismissal


def dismiss(request, label):
    
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    
    if label not in settings.REMINDERS:
        return Http404()
    
    dismiss_type = settings.REMINDERS[label].get("dismissable", "session")
    
    if dismiss_type == "session":
        request.session[label] = "dismissed"
        status = 200
    elif dismiss_type == "permanent":
        Dismissal.objects.create(user=request.user, label=label)
        status = 200
    else:
        status = 409
    
    return HttpResponse(status=status)
