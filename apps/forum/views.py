# coding=utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import ThemeCommentForm
from .models import Theme
from core.models import Setup
from django.conf import settings

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
        'meta_title': settings.FORUM_META_TITLE,
        'meta_desc': settings.FORUM_META_DESC,
        'meta_keys': settings.FORUM_META_KEYS,
    })


def theme_detail(request, slug):
    try:
        setup = Setup.objects.all()[0]
    except:
        setup = None
    theme_qs = Theme.objects.get(slug=slug)

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
