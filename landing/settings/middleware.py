from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
from django.conf import settings

__author__ = 'alexy'


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'countdown.context_processors.timer.countdown',
    'core.context_processors.travels.travels',
    'core.context_processors.page.current_page',
)
