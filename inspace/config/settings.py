import os

from dj_database_url import parse as parse_db_url
from prettyconf import config


# Project Structure
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(BASE_DIR))
FRONTEND_DIR = os.path.join(BASE_DIR, 'frontend')

# Project Info
PROJECT_NAME = 'InSpace - knowledge sharing'
PROJECT_DOMAIN = config('PROJECT_DOMAIN')
PROJECT_URL = 'http://{}'.format(PROJECT_DOMAIN)

# Debug & Development
DEBUG = config('DEBUG', default=False, cast=config.boolean)

# Database
default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
DATABASES = {
    'default': config('DATABASE_URL', default=default_dburl, cast=parse_db_url),
}

# Security & Signup/Signin
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=config.list)
SECRET_KEY = config('SECRET_KEY')


# i18n & l10n
TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = False
USE_TZ = True
LANGUAGE_CODE = 'en-us'
LANGUAGES = (
    ('en', 'English'),
    ('pt-br', 'Português (Brasil)'),
)
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)


# Media & Static
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(FRONTEND_DIR, 'media')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(FRONTEND_DIR, 'static_deploy')
STATIC_DIR = os.path.join(FRONTEND_DIR, 'static')

STATICFILES_DIRS = (
    ('styles', '%s/styles' % STATIC_DIR),
    ('js', '%s/js' % STATIC_DIR),
)


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (
            os.path.join(FRONTEND_DIR, 'templates'),
        ),
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': config('TEMPLATE_DEBUG', default=DEBUG, cast=config.boolean),
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'
APPEND_SLASH = True

WSGI_APPLICATION = 'config.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
