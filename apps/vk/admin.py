# coding=utf-8
from django.contrib import admin
from .models import VkUser


__author__ = 'alexy'


class VkUserAdmin(admin.ModelAdmin):
    list_display = ('profile_id', 'link', 'name', 'city', 'ip', 'date')


admin.site.register(VkUser, VkUserAdmin)

