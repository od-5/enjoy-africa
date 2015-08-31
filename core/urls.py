# coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib.auth.views import logout

__author__ = 'Rylcev Alexy'


urlpatterns = patterns(
    'core.views',
    url(r'^$', 'home', name='home'),
    url(r'^ticket/', 'ticket', name='form'),
    url(r'^accounts/registration/$', 'landing_registration', name='registration'),
    url(r'^accounts/login/$', 'landing_login', name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
)
