from .base import *

DEBUG = True

ADMINS = (
    ('Antonio M', 'email@mydomain.com'),
)

ALLOWED_HOSTS = ['.educaproject.com']

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'educa',
       'USER': 'postgres',
       'PASSWORD': 'Sergeevich2045',
   }
}

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True