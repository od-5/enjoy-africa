# coding=utf-8
from django.contrib import admin
from .models import Ticket, Setup, Slider, Review

# Register your models here.

class TicketAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created')


class SetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'email')

class SliderAdmin(admin.ModelAdmin):
    list_display = ('pic', )

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'pic', )

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Setup, SetupAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Review, ReviewAdmin)