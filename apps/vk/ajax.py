# coding=utf-8
from annoying.decorators import ajax_request
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from apps.travel.models import TravelReview
from .models import VkUser


@ajax_request
def check(request):
    if request.method == 'POST':
        profile_id = request.POST.get('profile_id')
        link = request.POST.get('profile_id')
        name = u'%s %s' % (request.POST.get('last_name'), request.POST.get('first_name'))
        ip = client_ip = request.META['REMOTE_ADDR']
        try:
            exist_user = VkUser.objects.get(profile_id=int(profile_id))
            return {
                'success': u'Уже посещал %s' % exist_user
            }
        except:
            exist_user = None
            return {
                'success': u'%s Ещё не посещал!' % exist_user
            }
    else:
        return {
            'success': u'Ошибка!'
        }
