import inspect

from django.contrib import admin
from django.db.models import Model

import app.models

# Register all models to admin page
# https://docs.djangoproject.com/en/1.10/intro/tutorial02/#make-the-poll-app-modifiable-in-the-admin
for key in dir(app.models):
    e = getattr(app.models, key)
    if inspect.isclass(e) and issubclass(e, Model):
        admin.site.register(e)

# admin.site.register(TimeOfSleep)
# admin.site.register(TwitterUsername)
