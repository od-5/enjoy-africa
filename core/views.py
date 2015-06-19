# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
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
    return render(request, 'base.html', {'setup': setup, 'form': form, 'slider': slider, 'review': review })

def ticket(request):
    try:
        email = Setup.objects.all()[0].email
    except:
        email = 'od-5@yandex.ru'
    if request.method == "POST":
        form = TicketForm(data=request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
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
        return HttpResponse(ticket.email)

    return HttpResponse('fail')