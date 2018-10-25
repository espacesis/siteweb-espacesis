"""
This is the settings file used by your live production server(s). That is, the
server(s) that host the real live website. This file contains production-level
settings only. It is sometimes called prod.py.
"""

"""
This settings is use in production
for the WGSI server as heroku.com
"""

#manage database (postgres)
# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME' : 'ikalaweb_prod_lunazik1',
        'USER' : 'i_ka_la_6565',
        'PASSWORD' : '7ekurity3rong',
        'HOST' : 'localhost',
        'PORT' : '',
    }
}

#all default seetings
from .base import *

#Warning : only in production
DEBUG = False
TEMPLATE_DEBUG = False

SECRET_KEY = '&)v83&m7v+0^)d2rq&n!_cp80pw+bmb2zqxre47jv+#ce2p#gz'

#how to access our site
ALLOWED_HOSTS = ['www.lunazik.com', '67.205.150.215']


# STATIC
# ------------------------
#MIDDLEWARE = MIDDLEWARE + ['whitenoise.middleware.WhiteNoiseMiddleware']
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ADMINS = (
    ('jeanluc kabulu', 'jeanluc.kabulu@gmail.com'),('jeanluc kabulu', 'jeanluc.kabulu@outlook.fr')
)

MANAGERS = ADMINS

"""
# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-ssl-redirect
SECURE_SSL_REDIRECT = True
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-secure
SESSION_COOKIE_SECURE = True
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-secure
CSRF_COOKIE_SECURE = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/topics/security/#ssl-https
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-seconds
# TODO: set this to 60 seconds first and then to 518400 once you prove the former works
SECURE_HSTS_SECONDS = 60

"""
