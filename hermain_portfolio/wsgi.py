"""
WSGI config for hermain_portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hermain_portfolio.settings")

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
