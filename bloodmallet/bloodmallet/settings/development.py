# -*- coding: utf-8 -*-
import os

from .common import *     # pylint: disable=unused-wildcard-import

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.join(BASE_DIR, '..')

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]

# logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s %(levelname)s %(module)s / %(funcName)s:%(lineno)d - %(message)s',
        }, # "%(asctime)s - %(filename)s / %(funcName)s - %(levelname)s - %(message)s"

    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'default',
            'filename':  os.path.join(BASE_DIR, 'debug.log'),
        },
        'console': {
            'level': 'DEBUG' if DEBUG else 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
    },
    'loggers': {
        'django': {
            'handlers': [
                # 'console',
                'file',
            ],
            'level': 'DEBUG',
            'propagate': True,
        },
        'general_website': { # add app to logger!
            'handlers': [
                'console', 'file'
            ],
            'level': 'DEBUG' if DEBUG else 'INFO',
            'propagate': True,
        },
        'compute_api': { # add app to logger!
            'handlers': [
                'console', 'file'
            ],
            'level': 'DEBUG' if DEBUG else 'INFO',
            'propagate': True,
        }
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
import pymysql
pymysql.install_as_MySQLdb()
from .secrets import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'OPTIONS': {
            'charset': 'utf8mb4'
        },
    }
}

# used to serve files from this path in non-debug production
STATIC_ROOT = 'static'

# SASS settings
SASS_PRECISION = 8
SASS_PROCESSOR_ROOT = STATIC_ROOT
# SASS_PROCESSOR_INCLUDE_FILE_PATTERN = r'^.+\.scss$'
# SASS_PROCESSOR_ENABLED = True

from .secrets import FILE_PATH_FIELD_DIRECTORY_DEV as FILE_PATH_FIELD_DIRECTORY
