"""
Django settings for setup project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path, os
from dotenv import load_dotenv
from django.contrib.messages import constants as messages
import pymysql

pymysql.install_as_MySQLdb()
load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = str(os.getenv('DJANGO_ALLOWED_HOSTS','127.0.0.1')).split(',')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'piemonte.apps.PiemonteConfig',
    'phonenumber_field',
    'widget_tweaks',
    'storages'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'setup.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'setup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

if str(os.getenv('DJANGO_ENV')) == 'production':
    CERT_PATH = '/etc/ssl/certs/BaltimoreCyberTrustRoot.crt.pem'
else:
    CERT_PATH = '/Users/pablobagano/Desktop/piemonte_v2/DigiCertGlobalRootCA.crt.pem'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': str(os.getenv('DB_NAME')),
        'USER': str(os.getenv('DB_USER')),
        'PASSWORD': str(os.getenv('DB_PASSWORD')), 
        'HOST': str(os.getenv('DB_HOST')),
        'PORT': '3306',
        'OPTIONS': {
            'ssl': {
                'ca': '/Users/pablobagano/Desktop/piemonte_v2/DigiCertGlobalRootCA.crt.pem',  # Use the CERT_PATH variable you defined earlier
            },
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

AZURE_ACCOUNT_NAME = str(os.getenv('AZURE_ACCOUNT_NAME'))
AZURE_ACCOUNT_KEY = str(os.getenv('AZURE_ACCOUNT_KEY')) 
AZURE_CONTAINER = str(os.getenv('AZURE_CONTAINER'))

#Use Azure Storage as backend for static files storage 
STATICFILES_STORAGE = 'storages.backends.azure_storage.AzureStorage'

#Azure Blob Domain and static URL 
AZURE_DOMAIN = f"{AZURE_ACCOUNT_NAME}.blob.core.windows.net"
STATIC_URL = f"https://{AZURE_DOMAIN}/{AZURE_CONTAINER}/"

# Local static settings (for reference or local development)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'setup/static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Messages 
# MESSAGE_TAGS = { 
#     messages.ERROR = 'fail',
#     messages.SUCCESS = 'success'
# }