# coding=utf-8
"""
core.settings.contrib
"""
# needed so cartridge gets correct currency
import locale
from .base import *  # noqa

# Extra installed apps - grapelli needs to be added before others
INSTALLED_APPS += (
     'channels',
     'rest_framework'
)

ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_SIGNUP_FORM_CLASS = 'base.forms.SignupForm'
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'

locale.setlocale(locale.LC_ALL, 'en_ZA.UTF-8')

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
