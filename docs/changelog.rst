.. _changelog:

ChangeLog
=========

0.2
---

- added permanent dismissals

Migrations
^^^^^^^^^^

Here is a sample migration that should work with Postgresql/nashvegas::

    ### New Model: reminders.Dismissal
    CREATE TABLE "reminders_dismissal" (
        "id" serial NOT NULL PRIMARY KEY,
        "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
        "label" varchar(200) NOT NULL,
        "dismissed_at" timestamp with time zone NOT NULL
    )
    ;
    CREATE INDEX "reminders_dismissal_user_id" ON "reminders_dismissal" ("user_id");


0.1
---

- initial release
