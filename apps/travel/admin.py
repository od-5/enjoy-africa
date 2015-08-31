# coding=utf-8
from django.contrib import admin
from .models import Travel, TravelReview, TravelReviewComment


__author__ = 'alexy'


class TravelAdmin(admin.ModelAdmin):
    list_display = ('title',)


class TravelReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'travel', 'user',)

admin.site.register(Travel, TravelAdmin)
admin.site.register(TravelReview, TravelReviewAdmin)
admin.site.register(TravelReviewComment)
