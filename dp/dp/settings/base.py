import os

here = lambda * x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)
PROJECT_ROOT = here("..")
root = lambda * x: os.path.join(os.path.abspath(PROJECT_ROOT), *x)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ("Chris Jones", "chris@brack3t.com"),
    ("Kenneth Love", "kenneth@brack3t.com")
)

MANAGERS = ADMINS

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}

# Social Auth
TWITTER_CONSUMER_KEY = ""
TWITTER_CONSUMER_SECRET = ""

GITHUB_APP_ID = ""
GITHUB_API_SECRET = ""

SOCIAL_AUTH_ERROR_KEY = "social_errors"
SOCIAL_AUTH_COMPLETE_URL_NAME = "socialauth_complete"
SOCIAL_AUTH_ASSOCIATE_URL_NAME = "socialauth_associate_complete"
SOCIAL_AUTH_DEFAULT_USERNAME = "new_social_auth_user"
SOCIAL_AUTH_EXTRA_DATA = False

LOGIN_REDIRECT_URL = "/profile/"
LOGIN_URL = "/login/"

POSTMAN_DISALLOW_ANONYMOUS = False
POSTMAN_DISALLOW_MULTIRECIPIENTS = True
POSTMAN_DISALLOW_COPIES_ON_REPLY = True
POSTMAN_AUTO_MODERATE_AS = True
POSTMAN_NOTIFIER_APP = None

EMAIL_USE_TLS = False
EMAIL_HOST = "localhost"
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 1025

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "America/Los_Angeles"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = root("../..", "media")
MEDIA_URL = "http://media.djangopeople.me/"

STATIC_ROOT = root("../..", "static")
STATIC_URL = "http://static.djangopeople.me/"

# Additional locations of static files
STATICFILES_DIRS = (
    root("staticfiles"),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
#    "django.contrib.staticfiles.finders.DefaultStorageFinder",
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = "lw&amp;jop%#cu#5ko%%d1h66r@^+ug5vnjqdt2-3#(2j+f+&amp;vmqk("

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
#     "django.template.loaders.eggs.Loader",
)

MIDDLEWARE_CLASSES = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "pagination.middleware.PaginationMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    "postman.context_processors.inbox",
)

AUTHENTICATION_BACKENDS = (
    "social_auth.backends.twitter.TwitterBackend",
    "social_auth.backends.contrib.github.GithubBackend",
    "django.contrib.auth.backends.ModelBackend",
)

ROOT_URLCONF = "dp.urls"

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = "dp.wsgi.application"

TEMPLATE_DIRS = (
    root("..", "templates")
)

DJANGO_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    "django.contrib.gis",
)

THIRD_PARTY_APPS = (
    "braces",
    "crispy_forms",
    "floppyforms",
    "pagination",
    "postman",
    "social_auth",
    "south",
    "taggit",
)

OUR_APPS = (
    "generic",
    "profiles",
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + OUR_APPS

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler"
        }
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    }
}
