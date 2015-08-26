# coding=utf-8
from annoying.decorators import ajax_request
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from .models import Setup, Slider, Review
from .forms import TicketForm

# Create your views here.
def home(request):
    slider = Slider.objects.all()
    review = Review.objects.all()
    form = TicketForm()
    try:
        setup = Setup.objects.all()[0]
    except:
        setup = None
    return render(request, 'base.html', {
        'setup': setup,
        'form': form,
        'slider': slider,
        'review': review
    })


@csrf_exempt
def ticket(request):
    try:
        email = Setup.objects.all()[0].email
    except:
        email = 'od-5@yandex.ru'
    if request.method == "POST":
        form = TicketForm(data=request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.ticket_status = 1
            ticket.save()
            if ticket.comment:
                message = u'Имя: %s\nE-mail: %s\nСообщение: %s\n' % (ticket.name, ticket.email, ticket.comment)
            else:
                message = u'Имя: %s\nE-mail: %s\n' % (ticket.name, ticket.email)
            send_mail(
                u'enjoy-africa.ru - Заявка с сайта',
                message,
                settings.DEFAULT_FROM_EMAIL,
                [email, ]
            )
        return HttpResponse('true')

    return HttpResponse('fail')

@ajax_request
def landing_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    error = u'Вы ввели неверный e-mail или пароль'
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect(request.META['HTTP_REFERER'])
        else:
            return {
                'error': error
            }
    else:
        return {
            'error': error
        }

@ajax_request
def landing_registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            exist_user = User.objects.get(username=username)
        except:
            exist_user = None
        if exist_user:
            return {
                'error': u'Пользователь с таким email уже зарегистрирован в системе!'
            }
        else:
            user = User.objects.create_user(username, username, password)
            user.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            auth.login(request, user)
            return {
                'success': u'Вы успещно зарегистрировались на сайте!'
            }