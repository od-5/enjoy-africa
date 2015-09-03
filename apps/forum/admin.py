# coding=utf-8
from django.contrib import admin
from .models import Theme, ThemeComment


__author__ = 'alexy'


class ThemeAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created')


class ThemeCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'theme', 'created')

admin.site.register(Theme, ThemeAdmin)
admin.site.register(ThemeComment, ThemeCommentAdmin)
