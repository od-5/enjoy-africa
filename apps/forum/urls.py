# coding=utf-8
from django.conf.urls import patterns, url
from django.views.generic import CreateView
from apps.forum.models import Theme

__author__ = 'alexy'


urlpatterns = patterns(
    'apps.forum.views',

    # url(r'^review-change/(?P<slug>[\w-]+)$', UpdateView.as_view(model=TravelReview, template_name='travel/travel_change.html'), name='change'),
    url(r'^add/$', CreateView.as_view(model=Theme, template_name='forum/theme_add.html'), name='add'),
    url(r'^(?P<slug>[\w-]+)$', 'theme_detail', name='detail'),
    url(r'^', 'theme_list', name='list'),
)

