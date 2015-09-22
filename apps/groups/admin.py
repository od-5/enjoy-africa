# coding=utf-8
from django.contrib import admin
from .models import Groups, GroupsComment


__author__ = 'alexy'


class GroupsAdmin(admin.ModelAdmin):
    list_display = ('title', 'reserved', 'seats', 'travel_start', 'travel_end')
    fieldsets = [
        (None, {
            'fields': ['travel', 'title', 'description', 'reserved', 'seats', 'price', 'cover', 'travel_start', 'travel_end', 'slug', ]
        }),
        ('SEO', {
            'classes': ('collapse', ),
            'fields': ['meta_title', 'meta_keys', 'meta_desc']
        }),
    ]


class GroupsCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'groups', 'created')

admin.site.register(Groups, GroupsAdmin)
admin.site.register(GroupsComment, GroupsCommentAdmin)
