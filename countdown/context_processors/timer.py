# coding=utf-8
from django.core.context_processors import request
from countdown.models import Timer
import datetime


__author__ = 'alexy'

def countdown(request):
    try:
        queryset = Timer.objects.all()[0]
        end_date = queryset.date + datetime.timedelta(days=queryset.offset)
        text = queryset.text
    except:
        end_date = None
        text = ''
    return {
         'timer': end_date,
         'timer_text': text
     }
