.. _usage:

Usage
=====

After configuring the appropriate settings, you will need to implement any
of the callables that you listed in the `REMINDERS` setting. Once that has
been done, using django-reminders is as simple as using a single template
tag.

Example::

    {% load reminders_tags %}
    
    <h3>Reminders</h3>
    
    {% reminders request.user as user_reminders %}
    
    {% if user_reminders %}
        <ul>
            {% for reminder in user_reminders %}
                <li>{{ reminder }}</li>
            {% endfor %}
        </ul>
    {% else %}
        <p class="info">You have no reminders at this time.</p>
    {% endif %}
