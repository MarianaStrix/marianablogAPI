import os

from django.utils.translation import gettext_lazy as _

from .env import env

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


SECRET_KEY = env("SECRET_KEY")


DEBUG = env.bool("DEBUG")


ALLOWED_HOSTS = tuple(env.list("ALLOWED_HOSTS", default=[]))


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",

    "accounts",
    "posts",

    "allauth",
    "allauth.account",
    "recaptcha",
    "rest_auth",
    "rest_auth.registration",
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_swagger",

    "easy_thumbnails",
    "taggit",
    "taggit_serializer",
    "corsheaders",
]

SITE_ID = 1


MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "blogAPI.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR + "/templates/"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


WSGI_APPLICATION = "blogAPI.wsgi.application"


DATABASES = {
    "default": env.db(),
}


AUTH_USER_MODEL = "accounts.Account"


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locale"),
]
LANGUAGES = [
    ("en", _("English")),
    ("ru", _("Russian"))
]


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": env("REDIS_LOCATION"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": env("REDIS_PASSWORD"),
        }
    }
}


STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static/")


MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
STATICFILES_DIRS = [os.path.join(BASE_DIR, "assets/"), ]


# Avatar size
AVATAR_SIZE = 150


# Django-taggit
TAGGIT_CASE_INSENSITIVE = True


# E-mail
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = "Mariana's Blog <support@marianastrix.com>"


# reCaptcha
GR_CAPTCHA_SECRET_KEY = env("CAPTCHA_SECRET_KEY")


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': os.getenv('LOG_FILE', '/var/log/blog/log.log')
        }
    },
    'loggers': {
        'posts': {
            'handlers': ['file'],
            'level': os.getenv('LOG_LEVEL', 'INFO'),
        },
        'django': {
            'handlers': ['file'],
            'level': os.getenv('LOG_LEVEL', 'INFO'),
            'propagate': True,
        },
    }
}