# coding=utf-8
from django.db import models


__author__ = 'alexey'


class Timer(models.Model):

    class Meta:
        verbose_name = u'Таймер обрабтного отсчёта'
        verbose_name_plural = u'Таймер обрабтного отсчёта'
        app_label = 'countdown'

    def __unicode__(self):
        return u'Таймер на %s дней' % self.offset

    date = models.DateField(verbose_name=u'Дата запуска')
    cycle = models.BooleanField(verbose_name=u'Зациклить', default=True)
    offset = models.PositiveIntegerField(verbose_name=u'Кол-во дней', default=14)
    text = models.TextField(verbose_name=u'Текст')