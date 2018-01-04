"""
WSGI config for site_ project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""
#!/usr/bin/python3.4
import os
import sys

sys.path.append("/usr/local/lib/python3.4/dist-packages/")
sys.path.append("/var/www/site_/site_/")
from django.core.wsgi import get_wsgi_application


#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "site_/settings")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

application = get_wsgi_application()
