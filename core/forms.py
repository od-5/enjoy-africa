# coding=utf-8
from django.forms import ModelForm, HiddenInput, CharField
from .models import Ticket, Avatar

__author__ = 'Rylcev Alexy'


class TicketForm(ModelForm):
    class Meta:
        model = Ticket


class UserForm(ModelForm):
    class Meta:
        model = Avatar
        widgets = {
            'user': HiddenInput(),
        }
