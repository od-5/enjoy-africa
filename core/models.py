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
    timer = models.TextField(verbose_name=u'Код таймера', blank=True, null=True)
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


class Slider(models.Model):
    name = models.CharField(verbose_name=u'Название', max_length=256, blank=True)
    image = models.ImageField(upload_to='top_slider', verbose_name=u'Слайд')

    def __unicode__(self):
        if self.name:
            return self.name
        else:
            return u'Изожение %s' % self.id

    def pic(self):
        return '<img src="%s"/>' % self.image.url
    pic.allow_tags = True

    class Meta:
        verbose_name = u'Слайд'
        verbose_name_plural = u'Слайды'
        app_label = 'core'


class Review(Common):
    name = models.CharField(verbose_name=u'Имя', max_length=256)
    photo = models.ImageField(upload_to='review', verbose_name=u'Фотография')
    content = models.TextField(verbose_name=u'Текст')

    def __unicode__(self):
        return self.name

    def pic(self):
        return '<img src="%s"/>' % self.photo.url
    pic.allow_tags = True

    class Meta:
        verbose_name = u'Отзыв'
        verbose_name_plural = u'Отзывы'
        app_label = 'core'