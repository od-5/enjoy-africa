# coding=utf-8
from django.contrib import admin
from .models import Page

__author__ = 'alexy'

class PageAdmin(admin.ModelAdmin):
    list_display = ('page', 'meta_title', )
    fieldsets = [
        (None, {
            'fields': ['page', 'title', 'meta_title', 'meta_keys', 'meta_desc', ]
        }),
    ]
admin.site.register(Page, PageAdmin)
