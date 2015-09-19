# coding=utf-8
from django.db import models

__author__ = 'alexy'


class Common(models.Model):
    created = models.DateField(verbose_name=u'Дата создания', auto_now=True)
    meta_title = models.CharField(verbose_name=u'Заголовок SEO', max_length=150, null=True)  # Заголовок SEO
    meta_desc = models.CharField(verbose_name=u'Описание SEO', max_length=500, null=True)  # Описание SEO
    meta_keys = models.CharField(verbose_name=u'Ключевые слова', max_length=500, null=True)  # Ключевые слова SEO
