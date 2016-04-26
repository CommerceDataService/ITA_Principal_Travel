from .base import *
import os
import dj_database_url
from django.core.exceptions import ImproperlyConfigured


try:
    SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
except KeyError as e:
    raise ImproperlyConfigured("You must define DJANGO_SECRET_KEY in .env")

try:
    AWS_HOSTNAME = os.environ['AWS_HOSTNAME']
    ALLOWED_HOSTS = [AWS_HOSTNAME, 'travel.cds.commerce.gov', '.cds.commerce.gov']
except KeyError as e:
    raise ImproperlyConfigured("You must define AWS_HOSTNAME in .env")

try:
    DATABASES['default'] = dj_database_url.config(conn_max_age=600)
except Exception as e:
    raise ImproperlyConfigured("You must define DATABASE_URL in .env")
