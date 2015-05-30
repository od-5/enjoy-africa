# coding=utf-8
from django.conf.urls import patterns, include, url

__author__ = 'Rylcev Alexy'


urlpatterns = patterns(
    'core.views',
    url(r'^ticket/', 'ticket', name='form'),
)