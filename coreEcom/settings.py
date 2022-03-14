"""
Django settings for coreEcom project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""


from distutils.debug import DEBUG
from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ['SECRET_KEY']
SECRET_KEY = 'asdasdkjsdi676'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = os.environ['DEBUG']

ALLOWED_HOSTS = ["localhost","127.0.0.1","innerkomfort.com","www.innerkomfort.com","143.110.241.76"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
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

ROOT_URLCONF = 'coreEcom.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates' ],
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

WSGI_APPLICATION = 'coreEcom.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# db_from_env = dj_database_url.config(conn_max_age=600)
# DATABASES['default'].update(db_from_env)

# DATABASE_URL: os.environ['HEROKU_POSTGRESQL_NAVY_URL']

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'ecomdb',
            'USER': 'ecomuser',
            'PASSWORD': '10389Ycl',
            'HOST': 'localhost',
            'PORT': '',
        }
    }


#Django CSRF protection does this by ensuring any forms submitted (for logins, signups, and so on) to your project were created by your project and not a third party.
CSRF_COOKIE_SECURE = True

#cookies your project produces for activities, such as logins, will only work over an encrypted connection
SESSION_COOKIE_SECURE = True

#ensures third parties cannot inject scripts into your project
#Warning: Django’s documentation states you shouldn’t rely completely on SECURE_BROWSER_XSS_FILTER. Never forget to validate and sanitize input.
SECURE_BROWSER_XSS_FILTER = True

X_FRAME_OPTIONS = 'SAMEORIGIN'

# PREPEND_WWW = True

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

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'assets'), ]

if DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    MEDIA_ROOT = os.path.join(BASE_DIR, 'assets/images')
else:
    STATIC_ROOT = "/home/yuvi/myprojectdir/staticfiles"
    STATIC_ROOT = "/home/yuvi/myprojectdir/staticfiles/images"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#for contact us give your gmail id and password
# EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = os.environ['EMAIL_HOST']
# EMAIL_USE_TLS = 1
# EMAIL_PORT = 587
# EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER'] # this email will be used to send emails
# EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD'] # host email password required
# EMAIL_RECEIVING_USER = ['info@innerkomfort.com','support@webinoxmedia.com','yuvraj@neurosoftech.org'] # email on which you will receive messages sent from website