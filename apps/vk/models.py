# -*- coding: utf-8 -*-
from django.db import models

__author__ = 'alexy'


class VkUser(models.Model):
    class Meta:
        verbose_name = u'Вконтакте'
        verbose_name_plural = u'Вконтакте'
        app_label = 'vk'

    def __unicode__(self):
        return self.link

    profile_id = models.IntegerField(null=True, verbose_name=u'vk_id')
    link = models.CharField(max_length=256, verbose_name=u'Профиль')
    name = models.CharField(max_length=256, blank=True, null=True, verbose_name=u'Имя')
    city = models.CharField(max_length=256, blank=True, null=True, verbose_name=u'Город')
    ip = models.GenericIPAddressField(max_length=256, blank=True, null=True, verbose_name=u'IP-адрес')
    date = models.DateTimeField(auto_now=True, verbose_name=u'Дата посещения')

