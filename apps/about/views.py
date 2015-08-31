# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render
from core.models import Setup
from .models import About


__author__ = 'alexy'


def about_list(request):
    try:
        setup = Setup.objects.all()[0]
    except:
        setup = None
    qs = About.objects.all()

    return render(request, 'about/about_list.html', {
        'setup': setup,
        'about_list': qs,
    })
