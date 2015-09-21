﻿# coding=utf-8
"""
Django settings for landing project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*v8a)%ljj*@&mj^$@n2o(p1tt2yeq7a8))rz3yq4jyl6r$t$xy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['enjoy-africa.ru', 'www.enjoy-africa.ru']

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'admin@enjoy-africa.ru'
EMAIL_HOST = 'smtp.fullspace.ru'
EMAIL_HOST_USER = 'admin@enjoy-africa.ru'
EMAIL_HOST_PASSWORD = 'alena2010'

LOGIN_REDIRECT_URL = '/'

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'ckeditor',
    'core',
    'countdown',
    'apps.about',
    'apps.groups',
    'apps.travel',
    'apps.forum',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'countdown.context_processors.timer.countdown',
    'core.context_processors.travels.travels',
    'core.context_processors.page.current_page',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

ROOT_URLCONF = 'landing.urls'

WSGI_APPLICATION = 'landing.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, '../static'),
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Django Suit configuration example
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': u'ENJOY-AFRICA',
    'HEADER_DATE_FORMAT': 'l, j. F Y',
    'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    # 'SEARCH_URL': '/admin/auth/user/',
    # 'MENU_ICONS': {
    #    'sites': 'icon-leaf',
    #    'auth': 'icon-lock',
    # },
    # 'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    'MENU': (
        'sites',
        # {'app': 'auth', 'icon':'icon-lock', 'models': ('user', 'group')},
        {'label': u'Перейти на сайт', 'url': 'home' },
        {'label': u'Настройки', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group', 'core.setup', 'countdown.timer')},
        {'label': u'Аватарки', 'icon':'icon-user', 'models': ('core.avatar',)},
        {'label': u'Заявки', 'icon':'icon-user', 'models': ('core.ticket', 'core.groupticket', )},
        {'label': u'Продажи', 'icon':'icon-user', 'models': ('core.sale',)},
        {'label': u'Слайдер', 'icon':'icon-picture', 'models': ('core.slider',)},
        {'label': u'Отзывы', 'icon':'icon-comment', 'models': ('core.review',)},
        {'label': u'О нас', 'app': 'about'},
        {'label': u'Журнал путешествий', 'app': 'travel'},
        {'label': u'Групповые туры', 'app': 'groups'},
        {'label': u'Форум', 'app': 'forum'},
        {'label': u'enjoy-safari.ru', 'url': 'http://www.enjoy-safari.ru/admin'},
    ),

}

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_CONFIGS = {
    'default': {
        'width': 700,
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['FontSize', 'TextColor'],
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink', 'Image'],
            ['RemoveFormat', 'Source']
        ]
    },
}

FORUM_META_TITLE = u'Форум о Сафари по Африке'
FORUM_META_DESC = u'Часто интересующие вопросы о путешествии в Африку и ответы на них'
FORUM_META_KEYS = u'Форум'

GROUPS_META_TITLE = u'Групповые туры по Африке'
GROUPS_META_DESC = u'Групповые туры: групповое сафари по Уганде, Бюджетное классическое сафари по паркам найроби -масай мара - озеро найваша - амбосели - найроби'
GROUPS_META_KEYS = u'Групповые туры'

TRAVELS_META_TITLE = u'Журнал путешествий по Африке'
TRAVELS_META_DESC = u'Рассказы о путешествиях наших клиентов: отзыв о путешествии в Кению, плюсы и минусы сафари, лучшие пляжи в Кении'
TRAVELS_META_KEYS = u'Журнал путешествий'
