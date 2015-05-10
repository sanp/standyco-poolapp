"""
Django settings for poolapp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Get environment - load this yaml file first!
import yaml
f = open('%s/poolapp/deploy/environment.yaml' % (BASE_DIR))
environment_yaml = yaml.safe_load(f)
f.close()
ENV_NAME = environment_yaml['environment']

# General yaml settings
f = open('%s/poolapp/deploy/profiles.yaml' % (BASE_DIR))
settings = yaml.safe_load(f)
ENV_SETTINGS = settings[ENV_NAME]
f.close()

# Secret yamlsettings
f = open('%s/poolapp/deploy/secret.yaml' % (BASE_DIR))
SECRET_SETTINGS = yaml.safe_load(f)
f.close()

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.request',)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_SETTINGS['secret_key']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ENV_SETTINGS['debug']
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'poolapp/templates')]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize', # For number formatting
    'django.contrib.formtools', # For generating form-preview pages
    'localflavor', # For local formatting: phone numbers, us states, etc
    # Site apps
    'poolapp.apps.home',
    'poolapp.apps.post',
    'poolapp.apps.find',
    'poolapp.apps.forums',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'poolapp.urls'

WSGI_APPLICATION = 'poolapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

postgres_settings = ENV_SETTINGS['postgres']
pg_db_name = postgres_settings['db_name']
pg_user = postgres_settings['user']
pg_password = postgres_settings['password']
pg_host = postgres_settings['host']
pg_port = postgres_settings['port']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': pg_db_name,
        'USER': pg_user,
        'PASSWORD': pg_password, # Move this into separete yaml file
        'HOST': pg_host,
        'PORT': pg_port,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'

# Static asset configuration
import os
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)

# Heroku settings
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
