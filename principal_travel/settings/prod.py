from .base import *
import os
import dj_database_url
from django.core.exceptions import ImproperlyConfigured


try:
    SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
except KeyError as e:
    raise ImproperlyConfigured("You must define DJANGO_SECRET_KEY")

ALLOWED_HOSTS = ['ec2-52-207-245-215.compute-1.amazonaws.com']

try:
    DATABASES['default'] = dj_database_url.config(conn_max_age=600)
except Exception as e:
    raise ImproperlyConfigured("You must define DATABASE_URL")
