# coding=utf-8
from django.contrib import admin
from .models import Groups, GroupsComment


__author__ = 'alexy'


class GroupsAdmin(admin.ModelAdmin):
    list_display = ('title', 'reserved', 'seats', 'travel_start', 'travel_end')


class GroupsCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'groups', 'created')

admin.site.register(Groups, GroupsAdmin)
admin.site.register(GroupsComment, GroupsCommentAdmin)
