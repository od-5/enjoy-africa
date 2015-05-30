# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render
from .models import Setup
from .forms import TicketForm

# Create your views here.
def home(request):
    form = TicketForm()
    try:
        setup = Setup.objects.all()[0]
    except:
        setup = None
    return render(request, 'base.html', {'setup': setup, 'form': form})

def ticket(request):
    if request.method == "POST":
        form = TicketForm(data=request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse('ok')

    return HttpResponse('fail')