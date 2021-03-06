import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '9()(lzm)jdr$szjfdx8^^#j_6efj@d&$9pb6l2h&=udxom3(bn'

DEBUG = True
TEMPLATE_DEBUG = True

if DEBUG:
    # XXX Monkey patch is_secure_transport to allow development over insecure HTTP

    from warnings import warn
    warn(UserWarning("Monkey_patching oauthlib.oauth2:is_secure_transport to allow OAuth2 over HTTP. Never do this in production!"))

    fake_is_secure_transport = lambda token_url: True

    import oauthlib.oauth2
    import requests_oauthlib.oauth2_session
    import oauthlib.oauth2.rfc6749.parameters
    import oauthlib.oauth2.rfc6749.clients.base

    for module in [
        oauthlib.oauth2,
        requests_oauthlib.oauth2_session,
        oauthlib.oauth2.rfc6749.parameters,
        oauthlib.oauth2.rfc6749.clients.base,
    ]:
        module.is_secure_transport = fake_is_secure_transport

ALLOWED_HOSTS = ['ssoexample.tracon.fi']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'kompassi_oauth2_example',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'kompassi_oauth2.backends.KompassiOAuth2AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

ROOT_URLCONF = 'kompassi_oauth2_example.urls'

WSGI_APPLICATION = 'kompassi_oauth2_example.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'kompassi_oauth2_example.sqlite3'),
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console':{
            'level': 'DEBUG' if DEBUG else 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'celery': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'WARNING',
            'propagate': True
        },
        'kompassi_oauth2': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'WARNING',
            'propagate': True
        },
    }
}

LANGUAGE_CODE = 'fi-fi'

TIME_ZONE = 'Europe/Helsinki'

USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'

KOMPASSI_OAUTH2_AUTHORIZATION_URL = 'http://kompassi.dev:8000/oauth2/authorize'
KOMPASSI_OAUTH2_TOKEN_URL = 'http://kompassi.dev:8000/oauth2/token'
KOMPASSI_OAUTH2_CLIENT_ID = 'kompassi_insecure_test_client_id'
KOMPASSI_OAUTH2_CLIENT_SECRET = 'kompassi_insecure_test_client_secret'
KOMPASSI_OAUTH2_SCOPE = ['read']
KOMPASSI_API_V2_USER_INFO_URL = 'http://kompassi.dev:8000/api/v2/people/me'

LOGIN_URL = '/oauth2/login'
LOGOUT_URL = '/logout'
