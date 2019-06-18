"""
WSGI config for blogAPI project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
from blogAPI.settings.env import env


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogAPI.settings.' + env('ENVIRONMENT'))
application = get_wsgi_application()
