# coding=utf-8
from django.contrib import admin
from .models import Ticket, Setup

# Register your models here.

class TicketAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created')


class SetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'email')

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Setup, SetupAdmin)