# coding=utf-8
from django.contrib import admin
from .models import About


__author__ = 'alexy'


class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    fieldsets = [
        (None, {
            'fields': ['title', 'text', ]
        }),
        ('SEO', {
            'classes': ('collapse', ),
            'fields': ['meta_title', 'meta_keys', 'meta_desc']
        }),
    ]


admin.site.register(About, AboutAdmin)
