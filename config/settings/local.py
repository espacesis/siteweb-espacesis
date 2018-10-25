"""
This is the settings file that you use when you’re working on the project locally.
Local development-specific settings include DEBUG mode, log level, and
activation of developer tools like django-debug-toolbar.
"""
from .base import *

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6b-!so#uo_q*q+9f&arxkmjq*%)ey-&9$jq5675e07pn7jry@h'

ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
	"127.0.0.1",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME' : 'espacesis',
        'USER' : 'jeanluc',
        'PASSWORD' : 'MotDePasse',
        'HOST' : 'localhost',
        'PORT' : '',
    }
}


# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = 'localhost'
# https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = 1025
