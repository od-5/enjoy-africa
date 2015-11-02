# coding=utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import ThemeCommentForm
from .models import Theme
from core.models import Setup

__author__ = 'alexy'


def theme_list(request):
    try:
        setup = Setup.objects.all()[0]
    except:
        setup = None
    theme_qs = Theme.objects.all()
    return render(request, 'forum/theme_list.html', {
        'setup': setup,
        'theme_list': theme_qs,
    })


def theme_detail(request, slug):
    try:
        setup = Setup.objects.all()[0]
    except:
        setup = None
    theme_qs = get_object_or_404(Theme, slug=slug)

    if request.method == "POST":
        comment_form = ThemeCommentForm(request.POST)
        if comment_form.is_valid():
            new_review = comment_form.save()
            new_review.save()
            return HttpResponseRedirect(request.path)
    else:
        if request.user.is_authenticated():
            comment_form = ThemeCommentForm(
                initial={
                    'user': request.user,
                    'theme': theme_qs}
            )
        else:
            comment_form = ThemeCommentForm()

    return render(request, 'forum/theme_detail.html', {
        'setup': setup,
        'theme': theme_qs,
        'comment_form': comment_form,
    })
