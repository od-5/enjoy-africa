# coding=utf-8
from django.db import models

__author__ = 'alexy'


class Common(models.Model):
    created = models.DateField(verbose_name=u'Дата создания', auto_now=True)