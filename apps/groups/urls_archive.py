# coding=utf-8
from django.conf.urls import patterns, url

__author__ = 'alexy'


urlpatterns = patterns(
    'apps.groups.views',
    url(r'^', 'groups_archive_view', name='list'),
)
