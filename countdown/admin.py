# coding=utf-8
from django.contrib import admin
from .models import Timer


__author__ = 'alexey'


class TimerAdmin(admin.ModelAdmin):

    list_display = ['date', 'cycle', 'offset']


admin.site.register(Timer, TimerAdmin)