"""
Django settings for prattle project.

Generated by 'django-admin startproject' using Django 3.2.15.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os # Code Credit ITTIB by CI
import dj_database_url # Code Credit ITTIB by CI
if os.path.isfile('env.py'):# Code Credit ITTIB by CI
    import env # Code Credit ITTIB by CI

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates') # Code Credit ITTIB by CI

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY') # Code Credit ITTIB by CI

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

X_FRAME_OPTIONS = 'SAMEORIGIN' # Code Credit ITTIB by CI

ALLOWED_HOSTS = ['prattle22.herokuapp.com', 'localhost'] # Code Credit ITTIB by CI


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin', 
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites', # Code Credit ITTIB by CI
    'allauth', # Code Credit ITTIB by CI
    'allauth.account', # Code Credit ITTIB by CI
    'allauth.socialaccount', # Code Credit ITTIB by CI
    'cloudinary_storage', # Code Credit ITTIB by CI
    'django.contrib.staticfiles',# Code Credit ITTIB by CI
    'cloudinary', # Code Credit ITTIB by CI
    'django_summernote', # Code Credit ITTIB by CI
    'blog', # Code Credit ITTIB by CI
]

SITE_ID = 1 # Code Credit ITTIB by CI

LOGIN_REDIRECT_URL = '/' # Code Credit ITTIB by CI
LOGOUT_REDIRECT_URL = '/' # Code Credit ITTIB by CI

ACCOUNT_EMAIL_VERIFICATION = 'none' # Code Credit ITTIB by CI

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'prattle.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR], # Code Credit ITTIB by CI
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'prattle.wsgi.application'

# Code Credit ITTIB by CI
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/' # Code Credit ITTIB by CI
# Code Credit ITTIB by CI
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
# Code Credit ITTIB by CI
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# Code Credit ITTIB by CI
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/' # Code Credit ITTIB by CI
# Code Credit ITTIB by CI
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
