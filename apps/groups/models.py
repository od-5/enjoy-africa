# coding=utf-8
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from pytils.translit import slugify
from apps.travel.models import Travel
from core.base_model import Common, CommonPage

__author__ = 'alexy'


class Groups(Common, CommonPage):
    class Meta:
        verbose_name = u'Групповые туры'
        verbose_name_plural = u'Групповые туры'
        app_label = 'groups'
        ordering = ['-travel_start']

    def __unicode__(self):
        return u'Тур %s %s, с %s по %s' % (self.travel, self.title, self.travel_start, self.travel_end)

    def save(self):
        self.slug = slugify(self.title)
        super(Groups, self).save()

    def get_absolute_url(self):
        return u"/groups/%s" % self.slug

    travel = models.ForeignKey(to=Travel, verbose_name=u'Направление')
    title = models.CharField(max_length=255, verbose_name=u'Название', blank=True, null=True)
    description = RichTextField(verbose_name=u'Описание', blank=True, null=True)
    reserved = models.PositiveIntegerField(verbose_name=u'Забронировано мест', default=0)
    seats = models.PositiveIntegerField(verbose_name=u'Количество мест', default=0)
    price = models.PositiveIntegerField(verbose_name=u'Стоимость', default=0)
    cover = models.ImageField(verbose_name=u'Обложка', upload_to='groups/')
    travel_start = models.DateField(verbose_name=u'Прибытие', blank=True, null=True)
    travel_end = models.DateField(verbose_name=u'Отъезд', blank=True, null=True)
    slug = models.SlugField(max_length=100, verbose_name=u'url', blank=True)


class GroupsComment(Common):
    class Meta:
        verbose_name = u'Коментарий'
        verbose_name_plural = u'Комментарии'
        app_label = 'groups'

    def __unicode__(self):
        return u'%s %s' % (self.user, self.groups)

    user = models.ForeignKey(to=User, verbose_name=u'Пользователь')
    groups = models.ForeignKey(to=Groups, verbose_name=u'Групповой тур')
    text = RichTextField(verbose_name=u'Текст')
