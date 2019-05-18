import os
from decouple import config


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = config('DEBUG', default=True, cast=bool)
SECRET_KEY = config('SECRET_KEY', default=os.environ['SECRET_KEY'], cast=str)

MAIN_HOST = '127.0.0.1' if DEBUG else '.herokuapp.com'

ALLOWED_HOSTS = [MAIN_HOST,]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'todos',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'todo_configs.urls'

WSGI_APPLICATION = 'todo_configs.wsgi.application'


# Database settings
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST': config('DB_HOST'),
            'PORT': config('DB_PORT')
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    # {
        # 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
        # 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
        # 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
        # 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Template and static configs
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
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

STATIC_URL = '/www/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'www', 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
