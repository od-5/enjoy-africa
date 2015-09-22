# coding=utf-8
from ckeditor.fields import RichTextField
from django.db import models
from core.base_model import Common, CommonPage

__author__ = 'alexy'


class About(Common, CommonPage):
    class Meta:
        verbose_name = u'Статья'
        verbose_name_plural = u'Статьи'
        app_label = 'about'
        ordering = ['-created']

    def __unicode__(self):
        return self.title

    title = models.CharField(verbose_name=u'Заголовок', max_length=150)
    # meta_desc = models.CharField(verbose_name=u'Описание', max_length=500, null=True) #Описание SEO
    # meta_keys = models.CharField(verbose_name=u'Ключевые слова', max_length=500, null=True) #Ключевые слова SEO
    text = RichTextField(verbose_name=u'Текст')


class AboutSEO(Common):
    verbose_name = u'Настройки'
    verbose_name_plural = u'Настройки'
    app_label = 'about'
    ordering = ['-created']