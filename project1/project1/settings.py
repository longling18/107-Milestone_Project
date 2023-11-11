
from pathlib import Path
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xx57j#l-7q$-@w!jhzze8c9b&0(l+w2u4u5g5$bnrc)^i#t3f+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['univoice.netlify.app', '127.0.0.1', 'univoice.edu.ph']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'projectapp.apps.ProjectappConfig',
    'bootstrap5',
    'captcha',
    'django_session_timeout'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    'django_auto_logout.middleware.auto_logout',
]

ROOT_URLCONF = 'project1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'django_auto_logout.context_processors.auto_logout_client',
            ],
        },
    },
]

WSGI_APPLICATION = 'project1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'UniVoiceDb',
        'USER': 'postgres',
        'PASSWORD': 'himo2023',
        'HOST': 'localhost',
        'PORT': '2023',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Keep the default ModelBackend
    'projectapp.custom_auth_backend.CustomBackend',  # Replace 'yourapp' with the actual app name
]
# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Manila'

USE_L1ON = True

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

STATICFILES_DIRS = [BASE_DIR / "projectapp/static"]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AUTH_USER_MODEL = 'projectapp.CustomUser'

RECAPTCHA_PUBLIC_KEY = '6LdoRE0oAAAAAK0XwRm4zKRREvHyzDweAsK0qXPO'
RECAPTCHA_PRIVATE_KEY = '6LdoRE0oAAAAAIsVJX2byJJpSMQaGii9zGmotyNV'
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'login'
#Session time out

AUTO_LOGOUT = {'IDLE_TIME': 900, 'REDIRECT_TO_LOGIN_IMMEDIATELY': True,

'MESSAGE': 'The session has expired. Please login again to continue.',
}

SESSION_EXPIRE_SECONDS = 900 # 15 minutes (adjust this value as needed)
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True


#EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
#EMAIL_FILE_PATH = BASE_DIR / "sent_emails"

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'sheinaqueenhimo@gmail.com'
EMAIL_HOST_PASSWORD = 'himo123123'
