import os
from .settings import *

# Configure the domain name using the environment variable
# that Azure automatically creates for us.
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []

CSRF_TRUSTED_ORIGINS = ['https://'+ os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []
DEBUG = False
DEBUG_PROPAGATE_EXCEPTIONS = True

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Configure database connection for Azure PostgreSQL instance.
# DBHOST is only the server name, not the full URL
# The full username for PostgreSQL flexible server is username (not @server-name).
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['AZURE_POSTGRESQL_DATABASE'],
        'HOST': os.environ['AZURE_POSTGRESQL_HOST'],
        'USER': os.environ['AZURE_POSTGRESQL_USERNAME'],
        'PASSWORD': os.environ['AZURE_POSTGRESQL_PASSWORD'], 
    }
}