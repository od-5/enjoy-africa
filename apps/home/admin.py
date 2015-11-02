# coding=utf-8
from django.contrib import admin
from suit.admin import SortableModelAdmin
from .models import Block3, Block10, Header, Attendant, AttendantItem


__author__ = 'alexy'


class Block3Admin(SortableModelAdmin):
    list_display = ('title', 'text', 'icon')
    ordering = ['order', ]


class Block10Admin(SortableModelAdmin):
    list_display = ('text', 'icon')
    ordering = ['order', ]


class HeaderAdmin(admin.ModelAdmin):
    list_display = ('text', 'block')


class AttendantItemInline(admin.StackedInline):
    model = AttendantItem


class AttendantAdmin(admin.ModelAdmin):
    inlines = [AttendantItemInline]


admin.site.register(Block3, Block3Admin)
admin.site.register(Block10, Block10Admin)
admin.site.register(Header, HeaderAdmin)
admin.site.register(Attendant, AttendantAdmin)
