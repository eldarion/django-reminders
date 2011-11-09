.. _installation:

Installation
============

* To install django-reminders::

    pip install django-reminders

* Add ``'reminders'`` to your ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
        # other apps
        "reminders",
    )

* Finally (and optionally if you configure all your reminders to not be
  dismissable)::

    ...
    url(r"^reminders/", include("reminders.urls")),
    ...
