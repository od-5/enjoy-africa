# coding=utf-8
from django.contrib import admin
from .models import Travel, TravelReview, TravelReviewComment


__author__ = 'alexy'


class TravelAdmin(admin.ModelAdmin):
    list_display = ('title',)


class TravelReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'travel', 'user',)
    fieldsets = [
        (None, {
            'fields': ['user', 'travel', 'title', 'image', 'text', 'moderated', 'slug', ]
        }),
        ('SEO', {
            'classes': ('collapse', ),
            'fields': ['meta_title', 'meta_keys', 'meta_desc']
        }),
    ]

admin.site.register(Travel, TravelAdmin)
admin.site.register(TravelReview, TravelReviewAdmin)
admin.site.register(TravelReviewComment)
