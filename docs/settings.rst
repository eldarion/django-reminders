.. _settings:

Settings
========


REMINDERS
---------

This app is driven by a list of callables and associated messages
configured by this setting. Here is an example::

    from emailconfirmation.reminders import confirmed
    
    REMINDERS = [
        {
            "label": "profile_completed",
            "test": "profiles.reminders.completed",
            "message": "You have only completed %(percentage)s%% of your <a href="%(url)s">profile</a>."
        },
        {
            "label": "email_confirmed",
            "test": lambda user: confirmed(user),
            "message": "Please <a href="%(url)">confirm</a> your email address."
        }
    ]


REMINDERS_DISMISSABLE
---------------------

:Default: True

If set to false then reminders will not be able to be dismissed. If set to
True, which is the default, then reminders can be dismissed for the duration
of the user's session.



Callable API
^^^^^^^^^^^^

This callables may be provided by third-party apps or may be defined by you,
the site developer. In either case, they should follow the following
conventions::

    def name(user):
        if there_is_stuff_for(user):
            return build_up_dict_for(user)

The message in the tuple with this callable will need to know what data is
being supplied by the callable. If there isn't a reminder, then the callable
should return None.
