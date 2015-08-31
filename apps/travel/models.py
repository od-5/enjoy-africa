# coding=utf-8
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from pytils.translit import slugify
from core.models import Common


__author__ = 'alexy'


class Travel(Common):
    class Meta:
        verbose_name = u'Направление'
        verbose_name_plural = u'Направления'
        app_label = 'travel'
        ordering = ['-id']

    def __unicode__(self):
        return self.title

    def save(self):
        self.slug = slugify(self.title)
        super(Travel, self).save()

    def get_absolute_url(self):
        return u"/travels/%s" % self.slug

    title = models.CharField(verbose_name=u'Заголовок', max_length=150)
    text = RichTextField(verbose_name=u'Текст', blank=True, null=True)
    slug = models.SlugField(max_length=100, verbose_name=u'url', blank=True)


class TravelReview(Common):
    class Meta:
        verbose_name = u'Статья'
        verbose_name_plural = u'Статьи'
        app_label = 'travel'

    def __unicode__(self):
        return self.title

    def save(self):
        self.slug = slugify(self.title)
        super(TravelReview, self).save()

    def get_absolute_url(self):
        return u"/travels/review/%s" % self.slug

    user = models.ForeignKey(to=User, verbose_name=u'Пользователь')
    travel = models.ForeignKey(to=Travel, verbose_name=u'направление')
    title = models.CharField(verbose_name=u'Заголовок', max_length=255)
    image = models.ImageField(verbose_name=u'Обложка', upload_to='travels/')
    text = RichTextField(verbose_name=u'Текст')
    moderated = models.BooleanField(verbose_name=u'Одобрено', default=False)
    slug = models.SlugField(max_length=100, verbose_name=u'url', blank=True)


class TravelReviewComment(Common):
    class Meta:
        verbose_name = u'Коментарий'
        verbose_name_plural = u'Комментарии'
        app_label = 'travel'

    user = models.ForeignKey(to=User, verbose_name=u'Пользователь')
    travel_review = models.ForeignKey(to=TravelReview, verbose_name=u'Статья')
    text = RichTextField(verbose_name=u'Текст')