# coding=utf-8
import os
from .base import BASE_DIR

__author__ = 'alexy'


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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '../media')

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