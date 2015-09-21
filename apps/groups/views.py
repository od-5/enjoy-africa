# coding=utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from apps.forum.models import Theme
from apps.groups.forms import GroupsCommentForm
from apps.groups.models import Groups
from core.models import Setup
from datetime import date
from django.conf import settings

__author__ = 'alexy'


def groups_view(request):
    try:
        setup = Setup.objects.all()[0]
    except:
        setup = None
    groups_qs = Groups.objects.filter(travel_start__gte=date.today())

    date_sort = request.GET.get('date_sort')
    if date_sort:
        if date_sort == 'lt':
            groups_qs = groups_qs.order_by('-travel_start')
        else:
            groups_qs = groups_qs.order_by('travel_start')
    price_sort = request.GET.get('price_sort')
    if price_sort:
        if price_sort == 'lt':
            groups_qs = groups_qs.order_by('-price')
        else:
            groups_qs = groups_qs.order_by('price')

    theme_qs = Theme.objects.all()[:5]
    return render(request, 'groups/group_list.html', {
        'setup': setup,
        'group_list': groups_qs,
        'theme_list': theme_qs,
        'meta_title': settings.GROUPS_META_TITLE,
        'meta_desc': settings.GROUPS_META_DESC,
        'meta_keys': settings.GROUPS_META_KEYS,
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
