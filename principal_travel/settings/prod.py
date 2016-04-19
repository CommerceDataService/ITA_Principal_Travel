from .base import *
import os
from django.core.exceptions import ImproperlyConfigured


try:
    SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
except KeyError as e:
    raise ImproperlyConfigured("You must define DJANGO_SECRET_KEY")

ALLOWED_HOSTS = ['ec2-52-207-245-215.compute-1.amazonaws.com']

try:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'traveltracker',
            'USER': 'cdsadmin',
            'HOST': 'localhost',
            'PORT': 5432,
            'PASSWORD': os.environ['DJANGO_DB_PASSWORD'],
        }
    }
except KeyError as e:
    raise ImproperlyConfigured("You must define DJANGO_DB_PASSWORD.")
