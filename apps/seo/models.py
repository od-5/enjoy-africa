# coding=utf-8
from ckeditor.fields import RichTextField
from django.db import models
from core.base_model import CommonPage


__author__ = 'alexy'


class Page(CommonPage):
    class Meta:
        verbose_name = u'Страница'
        verbose_name_plural = u'Страницы'
        app_label = 'seo'

    PAGE_CHOICES = (
        ('about', u'О нас'),
        ('travels', u'Журнал путешествий'),
        ('groups', u'Групповые туры'),
        ('groups-archive', u'Прошедшие групповые туры'),
        ('forum', u'Форум'),
    )

    def __unicode__(self):
        return self.get_page_display()

    page = models.CharField(max_length=100, choices=PAGE_CHOICES, unique=True, verbose_name=u'Название')
    title = models.CharField(max_length=260, verbose_name=u'Заголовок страницы', blank=True, null=True)
    top_text = RichTextField(verbose_name=u'Текст в начале страницы', blank=True, null=True)
