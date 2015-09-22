import os
import socket

__author__ = 'alexy'



BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

SECRET_KEY = '*v8a)%ljj*@&mj^$@n2o(p1tt2yeq7a8))rz3yq4jyl6r$t$xy'

# DEBUG = True
if socket.gethostname() == 'lanius':
    DEBUG = False
else:
    DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['enjoy-africa.ru', 'www.enjoy-africa.ru']

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'admin@enjoy-africa.ru'
EMAIL_HOST = 'smtp.fullspace.ru'
EMAIL_HOST_USER = 'admin@enjoy-africa.ru'
EMAIL_HOST_PASSWORD = 'alena2010'

LOGIN_REDIRECT_URL = '/'

ROOT_URLCONF = 'landing.urls'

WSGI_APPLICATION = 'landing.wsgi.application'

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True