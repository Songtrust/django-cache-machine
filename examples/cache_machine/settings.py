import os

import django

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
        'LOCATION': 'localhost:11211',
    },
}

TEST_RUNNER = 'django_nose.runner.NoseTestSuiteRunner'

DATABASES = {
    'default': {
        'NAME': os.environ.get('TRAVIS') and 'travis_ci_test' or 'cache_machine_devel',
        'HOST': os.environ.get('PGHOST'),
        'PORT': os.environ.get('PGPORT'),
        'USER': os.environ.get('PGUSER'),
        'PASSWORD': os.environ.get('PGPASSWORD'),
        'ENGINE': 'django.db.backends.postgresql',
    },
    'slave': {
        'NAME': 'cache_machine_devel',
        'ENGINE': 'django.db.backends.postgresql',
        'TEST': {
            'MIRROR': 'default'
        },
    },
    'master2': {
        'NAME': os.environ.get('TRAVIS') and 'travis_ci_test2' or 'cache_machine_devel2',
        'HOST': os.environ.get('PGHOST'),
        'PORT': os.environ.get('PGPORT'),
        'USER': os.environ.get('PGUSER'),
        'PASSWORD': os.environ.get('PGPASSWORD'),
        'ENGINE': 'django.db.backends.postgresql',
    },
    'slave2': {
        'NAME': 'cache_machine_devel2',
        'ENGINE': 'django.db.backends.postgresql',
        'TEST': {
            'MIRROR': 'master2'
        }
    },
}

INSTALLED_APPS = (
    'django_nose',
    'tests.testapp',
)

SECRET_KEY = 'ok'

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
