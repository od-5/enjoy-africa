# coding=utf-8
from django.conf.urls import patterns, url

__author__ = 'alexy'


urlpatterns = patterns(
    'apps.about.views',
    url(r'^', 'about_list', name='list'),
)