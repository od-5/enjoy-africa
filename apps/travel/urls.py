# coding=utf-8
from django.conf.urls import patterns, url

__author__ = 'alexy'


urlpatterns = patterns(
    'apps.travel.views',
    url(r'^', 'travel_list', name='list'),
)