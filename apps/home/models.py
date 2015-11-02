# -*- coding: utf-8 -*-
from django.db import models

__author__ = 'alexy'


class Block3(models.Model):
    class Meta:
        verbose_name = u'Почему именно мы'
        verbose_name_plural = u'Почему именно мы'
        app_label = 'home'

    def __unicode__(self):
        return self.title

    ICON_CHOICE = (
        ('block3-icon-posr', u'люди'),
        ('block3-icon-24h', u'24 часа'),
        ('block3-icon-zvuk', u'мегафон'),
        ('block3-icon-money', u'монеты'),
    )

    title = models.CharField(max_length=256, verbose_name=u'Заголовок')
    text = models.TextField(verbose_name=u'Текст')
    icon = models.CharField(max_length=50, default=ICON_CHOICE[0][0], choices=ICON_CHOICE)
    order = models.PositiveSmallIntegerField(default=1, verbose_name=u'Сортировка')


class Block10(models.Model):
    class Meta:
        verbose_name = u'Что включено в стоимость'
        verbose_name_plural = u'Что включено в стоимость'
        app_label = 'home'

    def __unicode__(self):
        return self.text

    ICON_CHOICE = (
        ('block10-icon-1', u'самолёт'),
        ('block10-icon-2', u'автомобиль'),
        ('block10-icon-3', u'дом'),
        ('block10-icon-4', u'гид'),
        ('block10-icon-6', u'мегафон'),
        ('block10-icon-7', u'монеты'),
        ('block10-icon-8', u'бутылка'),
        ('block10-icon-9', u'сим карта'),
    )

    text = models.TextField(verbose_name=u'Текст')
    icon = models.CharField(max_length=50, default=ICON_CHOICE[0][0], choices=ICON_CHOICE)
    order = models.PositiveSmallIntegerField(default=1, verbose_name=u'Сортировка')


class Header(models.Model):
    class Meta:
        verbose_name = u'Заголовок блока'
        verbose_name_plural = u'Заголовки блоков'
        app_label = 'home'

    def __unicode__(self):
        return self.text

    BLOCK_CHOICE = (
        (1, u'Первый блок'),
        (2, u'Почему именно мы'),
        (3, u'Первая форма с заявкой'),
        (4, u'Сопровождающий'),
        (5, u'4 шага'),
        (6, u'Первый информационный блок'),
        (7, u'Что включено в стоимость'),
        (8, u'Второй информационный блок'),
        (9, u'Отзывы о поездках'),
    )

    text = models.TextField(verbose_name=u'Текст')
    block = models.PositiveSmallIntegerField(default=1, choices=BLOCK_CHOICE, unique=True)


class Attendant(models.Model):
    class Meta:
        verbose_name = u'Наш сопровождающий'
        verbose_name_plural = u'Наш сопровождающий'
        app_label = 'home'

    def __unicode__(self):
        return self.text

    text = models.TextField(verbose_name=u'Текст')


class AttendantItem(models.Model):
    class Meta:
        verbose_name = u'Пункт'
        verbose_name_plural = u'Пункты'
        app_label = 'home'

    def __unicode__(self):
        return self.text

    ICON_CHOICE = (
        ('block5-icon-browser', u'Компас'),
        ('block5-icon-aircraft', u'Самолёт'),
        ('block5-icon-umbrella', u'Зонтик'),
        ('block5-icon-camera', u'Камера'),
    )

    attendant = models.ForeignKey(to=Attendant)
    text = models.TextField(verbose_name=u'Текст')
    icon = models.CharField(default=ICON_CHOICE[0][0], choices=ICON_CHOICE, max_length=50, verbose_name=u'Иконка')
