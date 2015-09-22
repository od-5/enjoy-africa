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
from .models import Setup, Slider, Review, Avatar
from .forms import TicketForm, UserForm


# Create your views here.
def home(request):
    slider = Slider.objects.all()
    review = TravelReview.objects.all()[:3]
    form = TicketForm()
    try:
        setup = Setup.objects.all()[0]
    except:
        setup = None
    return render(request, 'index.html', {
        'setup': setup,
        'form': form,
        'slider': slider,
        'review': review
    })


def profile_view(request):
    user = request.user
    if not user.is_authenticated():
        return HttpResponseRedirect('/')
    try:
        avatar = user.avatar.image
    except:
        avatar = None
    try:
        setup = Setup.objects.all()[0]
    except:
        setup = None

    if request.method == 'POST':
        data = request.POST.copy()
        email = data['email']
        first_name = data['first_name']
        last_name = data['last_name']
        user.first_name = first_name
        user.last_name = last_name
        if user.is_superuser:
            user.email = email
        else:
            user.email = user.username = email
        user.save()

        # form = UserForm(request.POST, request.FILES)
        # print form
        if user.avatar:
            profile = user.avatar
            form = UserForm(request.POST, request.FILES, instance=profile)
        else:
            form = UserForm(request.POST, request.FILES)
        # try:
        #     profile = user.avatar
        #     if request.FILES:
        #         print '******** has picture'
        #         profile.image = request.FILES['image']
        #     profile.description = data['description']
        #     profile.save()
        #     print '********** has avatar'
        # except:
        #     print '********** create new avatar'
        #     profile = form.save()
        #     profile.save()
        # return HttpResponseRedirect('/accounts/')
        if form.is_valid():
            print '*********** ok'
            avatar = form.save(commit=False)
            avatar.save()
        else:
            print '******** no ok'

        # if request.FILES or data['description']:
        #     print "check user avatar"
        #     try:
        #         print 'delete ***************'
        #         user.avatar.delete()
        #     except:
        #         pass
        #     form = UserForm(request.POST, request.FILES)
        #     if form.is_valid():
        #         print 'form save ************'
        #         if request.FILES:
        #             avatar = Avatar(user=user, image=request.FILES['image'], description=data['description'])
        #             avatar.save()
        #         return HttpResponseRedirect('/accounts/')




    return render(request, 'profile.html', {
        'setup': setup,
        'user': user,
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
            user.is_staff = True
            user.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            auth.login(request, user)
            return {
                'success': u'Вы успещно зарегистрировались на сайте!'
            }


def get_robots_txt(request):
    try:
        content = Setup.objects.all()[0].robots_txt
    except:
        content = u'User-agent: *'
    robots_response = HttpResponse(content, content_type='text/plain')
    return robots_response
