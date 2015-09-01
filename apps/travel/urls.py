# coding=utf-8
from django.conf.urls import patterns, url
from django.views.generic.edit import UpdateView, CreateView
from apps.travel.models import TravelReview

__author__ = 'alexy'


urlpatterns = patterns(
    'apps.travel.views',
    url(r'^review/(?P<slug>[\w-]+)$', 'travel_detail', name='detail'),
    url(r'^review-change/(?P<slug>[\w-]+)$', UpdateView.as_view(model=TravelReview, template_name='travel/travel_change.html'), name='change'),
    url(r'^review-add/$', CreateView.as_view(model=TravelReview, template_name='travel/travel_add.html'), name='add'),
    url(r'^', 'travel_list', name='list'),
)
