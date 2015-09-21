# coding=utf-8
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from apps.travel.forms import TravelReviewCommentForm
from core.models import Setup
from .models import Travel, TravelReview
from django.conf import settings

__author__ = 'alexy'


def travel_list(request):
    try:
        setup = Setup.objects.all()[0]
    except:
        setup = None
    travel_qs = Travel.objects.all()

    travel_review_qs = TravelReview.objects.all()

    travel = request.GET.get('travel')
    if travel:
        travel = int(travel)
        travel_review_qs = travel_review_qs.filter(travel=travel)
    author = request.GET.get('author')
    if author:
        travel_review_qs = travel_review_qs.filter(user=int(author))
    author_list = User.objects.filter(is_active=True)

    return render(request, 'travel/travel_list.html', {
        'setup': setup,
        'travel_list': travel_qs,
        'meta_title': settings.TRAVELS_META_TITLE,
        'meta_desc': settings.TRAVELS_META_DESC,
        'meta_keys': settings.TRAVELS_META_KEYS,
        'travel_review_list': travel_review_qs,
        'author_list': author_list,
        'travel_id': travel,
    })


def travel_detail(request, slug):
    try:
        setup = Setup.objects.all()[0]
    except:
        setup = None
    travel_qs = TravelReview.objects.get(slug=slug)
    if request.method == "POST":
        comment_form = TravelReviewCommentForm(request.POST)
        if comment_form.is_valid():
            new_review = comment_form.save()
            new_review.save()
            return HttpResponseRedirect(request.path)
    else:
        if request.user.is_authenticated():
            comment_form = TravelReviewCommentForm(
                initial={
                    'user': request.user,
                    'travel_review': travel_qs}
            )
        else:
            comment_form = TravelReviewCommentForm()

    return render(request, 'travel/travel_review_detail.html', {
        'setup': setup,
        'article': travel_qs,
        'comment_form': comment_form,
    })
