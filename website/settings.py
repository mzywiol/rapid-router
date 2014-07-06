"""
Django settings for O-Car-Go project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""


# Build paths inside the project like this: rel(rel_path)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
rel = lambda rel_path: os.path.join(BASE_DIR, rel_path)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xbq1u1w_zknl4t=wlem!)!)j*8=n9(2*wcxj$r6!b5#1uxgsv2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'website',
    'game',
    'reports',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nuit',
)

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'website.urls'

WSGI_APPLICATION = 'website.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Europe/London'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = rel('static')


# Required for admindocs

SITE_ID = 1


# PRESENTATION LAYER

NUIT_GLOBAL_TITLE = "Delivery Dash"
NUIT_GLOBAL_LINK = "/home/"


# Deployment

import os
if os.getenv('DEPLOYMENT', None):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': os.getenv('CLOUD_SQL_HOST'),
            'NAME': os.getenv('DATABASE_NAME'),
            'USER': 'root',
            'PASSWORD': os.getenv('CLOUD_SQL_PASSWORD'),
        }
    }
    COMPRESS_OFFLINE = True
    COMPRESS_ROOT = STATIC_ROOT
    COMPRESS_URL = STATIC_URL
elif os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine') or os.getenv('APPLICATION_ID', None):
    # Running on production App Engine, so use a Google Cloud SQL database.
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '/cloudsql/numeric-incline-526:db',
            'NAME': os.getenv('DATABASE_NAME'),
            'USER': 'root',
        }
    }
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'KEY_PREFIX': os.getenv('CACHE_PREFIX'),
            'TIMEOUT': 0,
        }
    }
    COMPRESS_OFFLINE = True
    COMPRESS_ROOT = STATIC_ROOT
    COMPRESS_URL = STATIC_URL
    # And require login for now
    MIDDLEWARE_CLASSES.append('website.middleware.loginrequired.LoginRequiredMiddleware')
    # inject the lib folder into the python path
    import sys
    lib_path = os.path.join(os.path.dirname(__file__), 'lib')
    if lib_path not in sys.path:
        sys.path.append(lib_path)
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': rel('dbfile'),
        }
    }
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': 'unique-snowflake'
        }
    }

# Keep this at the bottom
from django_autoconfig.autoconfig import configure_settings
configure_settings(globals())
