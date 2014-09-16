"""
WSGI config for superlists project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/

added import: django and django.setup() 9/12/2014 Carole
import django
django.setup()

"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "superlists.settings")


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
