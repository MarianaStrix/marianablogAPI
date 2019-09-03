import os

from django.core.wsgi import get_wsgi_application

from blogAPI.settings.env import env

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogAPI.settings.' + env('ENVIRONMENT'))
application = get_wsgi_application()
