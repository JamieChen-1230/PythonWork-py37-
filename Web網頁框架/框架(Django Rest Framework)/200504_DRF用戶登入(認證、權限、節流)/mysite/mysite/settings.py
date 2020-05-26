import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-4x67zni)%xsz05m3%^h%xjbzq5_2!*21ip$*w*z9yl55^t^*w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api.apps.ApiConfig',
    'rest_framework',
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

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

REST_FRAMEWORK = {
    # 全局使用認證類(若想讓view不使用全局認證類，則在其中加入authentication_classes=[])
    "DEFAULT_AUTHENTICATION_CLASSES": (
        'api.utils.auth.MyAuthentication',
    ),  # 通常不會寫到views中，而是會再另外創一個py檔(EX:auth.py)
    # 未通過身分認證的request.user 和 request.auth 的默認值
    'UNAUTHENTICATED_USER': None,
    'UNAUTHENTICATED_TOKEN': None,

    # 全局使用權限
    'DEFAULT_PERMISSION_CLASSES': (
        'api.utils.permission.SVIPPermission',
    ),  # 通常不會寫到views中，而是會再另外創一個py檔(EX:permission.py)

    # 全局使用節流器
    'DEFAULT_THROTTLE_CLASSES': (
        'api.utils.throttle.VisitThrottle',
    ),  # 通常不會寫到views中，而是會再另外創一個py檔(EX:throttle.py)
    # 使用內置的訪問節流器(SimpleRateThrottle)，需要設置訪問的頻率
    'DEFAULT_THROTTLE_RATES': {
        'ip': '3/m',   # ip為自定義字段，3/m表示一分鐘三次
        'username': '10/m',
    },  # 若繼承SimpleRateThrottle的話就必須設置

}
