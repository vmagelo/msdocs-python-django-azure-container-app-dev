import os
from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Don't use Whitenoise to avoid having to run collectstatic first.
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

ALLOWED_HOSTS = ['*']

# Configure connection setting for local PostgreSQL instance.
# Set these environment variables in the .env file for this project.  

# Allow local to use remote database without changing form of environment variables.
host = os.environ['DBHOST'] + ".postgres.database.azure.com" if 'REMOTE_POSTGRESQL' in os.environ else os.environ['DBHOST']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DBNAME'],
        'HOST': host,
        'USER': os.environ['DBUSER'],
        'PASSWORD': os.environ['DBPASS'],
    }
}
