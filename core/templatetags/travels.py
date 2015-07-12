from django.shortcuts import render_to_response
from django.utils.safestring import mark_safe
from core.models import Ticket
from core.context_processors.travels import WorkoutCalendar
from django import template

register = template.Library()

@register.simple_tag
def calendar(year, month):
  my_workouts = Ticket.objects.order_by('travel_start').filter(
    travel_start__year=year, travel_start__month=month
  )
  cal = WorkoutCalendar(my_workouts).formatmonth(year, month)
  return cal