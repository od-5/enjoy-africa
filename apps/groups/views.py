# coding=utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from apps.forum.models import Theme
from apps.groups.forms import GroupsCommentForm
from apps.groups.models import Groups
from core.models import Setup
from datetime import date

__author__ = 'alexy'


def groups_view(request):
    try:
        setup = Setup.objects.all()[0]
    except:
        setup = None
    groups_qs = Groups.objects.filter(travel_start__gte=date.today())
    theme_qs = Theme.objects.all()[:5]
    return render(request, 'groups/group_list.html', {
        'setup': setup,
        'group_list': groups_qs,
        'theme_list': theme_qs
    })


def groups_detail(request, slug):
    try:
        setup = Setup.objects.all()[0]
    except:
        setup = None
    group_qs = Groups.objects.get(slug=slug)

    if request.method == "POST":
        comment_form = GroupsCommentForm(request.POST)
        if comment_form.is_valid():
            new_review = comment_form.save()
            new_review.save()
            return HttpResponseRedirect(request.path)
    else:
        if request.user.is_authenticated():
            comment_form = GroupsCommentForm(
                initial={
                    'user': request.user,
                    'groups': group_qs}
            )
        else:
            comment_form = GroupsCommentForm()

    return render(request, 'groups/groups_detail.html', {
        'setup': setup,
        'group': group_qs,
        'comment_form': comment_form,
    })
