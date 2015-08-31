# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render
from core.models import Setup
from .models import Travel, TravelReview


__author__ = 'alexy'


def travel_list(request):
    try:
        setup = Setup.objects.all()[0]
    except:
        setup = None
    travel_qs = Travel.objects.all()
    travel_review_qs = TravelReview.objects.filter(moderated=True)

    return render(request, 'travel/travel_list.html', {
        'setup': setup,
        'travel_list': travel_qs,
        'travel_review_list': travel_review_qs,
    })
