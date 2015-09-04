# coding=utf-8
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from pytils.translit import slugify
from core.base_model import Common

__author__ = 'alexy'


class Theme(Common):
    class Meta:
        verbose_name = u'Тема'
        verbose_name_plural = u'Темы'
        app_label = 'forum'
        ordering = ['-created']

    def __unicode__(self):
        return self.title

    def save(self):
        self.slug = slugify(self.title)
        super(Theme, self).save()

    def get_absolute_url(self):
        return u"/forum/%s" % self.slug

    user = models.ForeignKey(to=User, verbose_name=u'Пользователь')
    title = models.CharField(max_length=255, verbose_name=u'Название')
    description = RichTextField(verbose_name=u'Описание')
    # file = models.FileField(verbose_name=u'Файл', upload_to='forum/', blank=True, null=True)
    slug = models.SlugField(max_length=100, verbose_name=u'url', blank=True)


class ThemeComment(Common):
    class Meta:
        verbose_name = u'Коментарий'
        verbose_name_plural = u'Комментарии'
        app_label = 'forum'
        ordering = ['created']

    def __unicode__(self):
        return u'%s %s' % (self.user, self.theme)

    user = models.ForeignKey(to=User, verbose_name=u'Пользователь')
    theme = models.ForeignKey(to=Theme, verbose_name=u'Текст')
    text = RichTextField(verbose_name=u'Текст')
