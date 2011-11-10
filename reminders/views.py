from django.conf import settings
from django.http import HttpResponse, Http404, HttpResponseNotAllowed


def dismiss(request, label):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    if label not in settings.REMINDERS:
        return Http404()
    if not settings.REMINDERS.get(label).get("dismissable", True):
        return HttpResponse(status=409)
    for reminder in settings.REMINDERS:
        if reminder == label and settings.REMINDERS[reminder].get("dismissable", True):
            request.session[label] = "dismissed"
    return HttpResponse()
