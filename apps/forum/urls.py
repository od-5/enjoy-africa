# coding=utf-8
from django.conf.urls import patterns, url

__author__ = 'alexy'


urlpatterns = patterns(
    'apps.forum.views',

    # url(r'^review-change/(?P<slug>[\w-]+)$', UpdateView.as_view(model=TravelReview, template_name='travel/travel_change.html'), name='change'),
    # url(r'^review-add/$', CreateView.as_view(model=TravelReview, template_name='travel/travel_add.html'), name='add'),
    # url(r'^', TemplateView.as_view(template_name='groups/group_list.html'), name='list'),
    url(r'^(?P<slug>[\w-]+)$', 'theme_detail', name='detail'),
    url(r'^', 'theme_list', name='list'),
)

