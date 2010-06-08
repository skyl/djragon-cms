import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'dev.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# For right now, we just use a simple structure with no staticfiles app
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "media")
#'/home/skyl/Code/github/Dragon-CMS/djragon_cms/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'xpva8t5)!lyo)$s2foayc@n2%li2gs%hi%)4sm!yknwl4pi3hd'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "staticfiles.context_processors.static_url",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
)
# hmm.. trying to plug in the news urls .. can't get no trailing slash to work..
#APPEND_SLASH = False

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, "templates"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.comments',
    #'grappelli', #mutherfuckin' raza fraza
    #http://github.com/wardi/django-filebrowser-no-grappelli, or not ...
    'staticfiles',
    'tinymce',
    'filebrowser',
    'django_extensions',

    'feincms',
    'mptt',
    'feincms.module.page',
    #'feincms.module.medialibrary', #nofilebrowser

    'dcms', # our central swiss-army app
    'content', # news, blogs, cio_focus, etc

    'tagging',
    'tagging_ext',

    # dev stuff
    #'south', # why not give it a try? .. uh, cause it sucks?
    #'debug_toolbar', #meh, no need to keep that on for default..

    #Queue
    'transcode',
    'celery',

    'djredis',
    'django.contrib.admin',
)

STATIC_ROOT = MEDIA_ROOT
STATIC_URL = MEDIA_URL

#fein
FEINCMS_ADMIN_MEDIA = '/media/feincms/'

#FEIN+tinymce
TINYMCE_JS_URL = '/media/tiny_mce/tiny_mce.js'
#TINYMCE_INIT_URL = '/media/admin/tinymce_setup/tinymce_setup.js'
#TINYMCE_JS_URL = 'http://debug.example.org/tiny_mce/tiny_mce_src.js'
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}
TINYMCE_SPELLCHECKER = True
#TINYMCE_COMPRESSOR = True


#URL_FILEBROWSER_MEDIA = '/media/filebrowser/'
# filebrowser settings
# http://code.google.com/p/django-filebrowser/wiki/Settings
FILEBROWSER_DEBUG = True
FILEBROWSER_MEDIA_ROOT = os.path.join(MEDIA_ROOT, 'filebrowser')
FILEBROWSER_MEDIA_URL = '/media/filebrowser/'
FILEBROWSER_DIRECTORY = 'uploads'
FILEBROWSER_MAX_UPLOAD_SIZE = 1000000000




#Celery, rabbitmq
BROKER_HOST = "localhost"
BROKER_PORT = 5672
BROKER_USER = "skyl"
from local_settings import BROKER_PASSWORD
BROKER_VHOST = "transcode"
#CELERY_RESULT_BACKEND = "amqp"
# CELERY_IMPORTS = ("transcode.tasks",)
#CELERY_CONCURRENCY

#Transcode settings
TRANSCODE_LOCAL = True

#debug_toolbar
#INTERNAL_IPS = ('127.0.0.1',)
#DEBUG_TOOLBAR_CONFIG = {
#    'INTERCEPT_REDIRECTS': False,
#}
