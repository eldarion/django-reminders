import datetime

from django.db import models

from django.contrib.auth.models import User


class Dismissal(models.Model):
    
    user = models.ForeignKey(User, related_name="reminder_dismissals")
    label = models.CharField(max_length=200)
    dismissed_at = models.DateTimeField(default=datetime.datetime.now)
