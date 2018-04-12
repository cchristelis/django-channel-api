
"""Configuration for production server"""
# noinspection PyUnresolvedReferences
from .prod import *  # noqa
import os
print(os.environ)

DEBUG = False

ALLOWED_HOSTS = ['*']

ADMINS = (
    ('Christian Christelis', 'christian@kartoza.com'),)
