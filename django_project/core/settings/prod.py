# coding=utf-8

"""Project level settings."""
from .project import *  # noqa
from .secret import SENTRY_DSN

# Comment if you are not running behind proxy
# USE_X_FORWARDED_HOST = True

# Set debug to false for production
DEBUG = TEMPLATE_DEBUG = False
TESTING = DEBUG

STATICFILES_FINDERS += (
    'compressor.finders.CompressorFinder',
)
