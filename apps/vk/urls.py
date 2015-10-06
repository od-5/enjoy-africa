# coding=utf-8
from django.conf.urls import patterns, url
from django.views.generic.edit import UpdateView, CreateView
from apps.travel.models import TravelReview

__author__ = 'alexy'


urlpatterns = patterns(
    'apps.vk.ajax',
    url(r'^check/$', 'check', name='check'),
)
