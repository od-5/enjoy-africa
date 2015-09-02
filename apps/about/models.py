# coding=utf-8
from ckeditor.fields import RichTextField
from django.db import models
from core.base_model import Common

__author__ = 'alexy'


class About(Common):
    class Meta:
        verbose_name = u'Статья'
        verbose_name_plural = u'Статьи'
        app_label = 'about'
        ordering = ['-created']

    def __unicode__(self):
        return self.title

    title = models.CharField(verbose_name=u'Заголовок', max_length=150)
    text = RichTextField(verbose_name=u'Текст')
