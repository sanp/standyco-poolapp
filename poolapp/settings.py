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

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.request',)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

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
    # storages and boto for hosting static files in amazing s3
    'storages',
    'boto',
    # Site apps
    'poolapp.apps.home',
    'poolapp.apps.post',
    'poolapp.apps.find',
    'poolapp.apps.forums',
    'poolapp.apps.about',
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

# Control what formats time data can be input in, so no need to set up special
# rules in models, forms, or javascript for converting time to appropriate
# format
TIME_INPUT_FORMATS = ['%H:%M', '%I:%M%p', '%I:%M %p']

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# Parse database configuration from $DATABASE_URL - for use with Heroku
# postgres DB
# TODO: Why isn't the dj_database_url config thing working.  WTF.
import dj_database_url
DATABASES = ENV_SETTINGS['databases']
# if ENV_NAME == 'production':
#   DATABASES = { 'default' : dj_database_url.config()}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Chicago'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static asset configuration
import os
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
# Place (outside of django project) where static files are collected -- should
# be different from staticfiles_dirs! I.e. where the static files are *output*
STATIC_ROOT = 'staticfiles'
# URL where static files can be found in browser. E.g.
# www.mywebsite.com/static/css/master.css, or something.
STATIC_URL = '/static/'

# Where in the application static files are *input*
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)

# Heroku settings
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

#Storage on S3 settings are stored as os.environs to keep settings.py clean
USE_AMW_FOR_STATICFILES = ENV_SETTINGS['use_amw_for_staticfiles']
if USE_AMW_FOR_STATICFILES:
  AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
  AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
  AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
  STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
  S3_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
  STATIC_URL = S3_URL

# For sending emails using gmail smtp server
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'standyco.inc@gmail.com'
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
