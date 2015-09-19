# coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib.auth.views import logout
from django.views.generic import TemplateView

__author__ = 'Rylcev Alexy'


urlpatterns = patterns(
    'core.views',
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain'), name="robots"),
    url(r'^sitemap\.xml$', TemplateView.as_view(template_name='sitemap.xml', content_type='text/plain'), name="sitemap"),
    url(r'^$', 'home', name='home'),
    url(r'^ticket/', 'ticket', name='form'),
    url(r'^accounts/$', 'profile_view', name='profile'),
    url(r'^accounts/registration/$', 'landing_registration', name='registration'),
    url(r'^accounts/login/$', 'landing_login', name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
)
