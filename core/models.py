# coding=utf-8
from django.db import models


# Create your models here.


class Common(models.Model):
    created = models.DateField(verbose_name=u'Дата создания', auto_now=True)


class Ticket(Common):
    name = models.CharField(verbose_name=u'Имя', max_length=256)
    email = models.EmailField(verbose_name=u'e-mail', max_length=256)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Заявка'
        verbose_name_plural = u'Заявки'
        app_label = 'core'


class Setup(models.Model):
    title = models.CharField(verbose_name=u'Заголовок <TITLE>...</TITLE>', max_length=256, blank=True)
    email = models.EmailField(verbose_name=u'e-mail для приёма заявок', blank=True)
    meta_key = models.TextField(verbose_name=u'Ключевые слова META_KEYWORDS', blank=True)
    meta_desc = models.TextField(verbose_name=u'Описание META_DESCRIPTION', blank=True)
    top_js = models.TextField(verbose_name=u'Скрипты в <HEAD>..</HEAD>', blank=True)
    bottom_js = models.TextField(verbose_name=u'Скрипты перед закрывающим </BODY>', blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Настройки сайта'
        verbose_name_plural = u'Настройки сайта'
        app_label = 'core'