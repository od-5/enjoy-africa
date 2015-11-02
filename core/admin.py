# coding=utf-8
from django.contrib import admin
from django.core.checks import messages
from django.core.exceptions import FieldError
from .models import Ticket, Setup, Slider, Review, Avatar
from django.forms import ModelForm
from suit.widgets import EnclosedInput, AutosizedTextarea


class TicketAdminForm(ModelForm):
    class Meta:
        widgets = {
            'comment': AutosizedTextarea,
            'ticket_comment': AutosizedTextarea,
        }


class TicketAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'group', 'created', 'ticket_status', 'ticket_comment')
    list_filter = ['email', 'created', 'ticket_status']
    search_fields = ['email', ]
    date_hierarchy = 'created'
    fields = ('name', 'email', 'comment', 'sale', 'ticket_status', 'ticket_comment')
    form = TicketAdminForm

    def get_queryset(self, request):
        return self.model.objects.filter(sale=False, group__isnull=True)

    def suit_row_attributes(self, obj, request):
        css_class = {
            1: 'success',
            0: 'warning',
            2: 'error',
        }.get(obj.ticket_status)
        if css_class:
            return {'class': css_class, 'data': obj.name}


class GroupTicket(Ticket):
    class Meta:
        proxy = True
        verbose_name = u'Групповая заявка'
        verbose_name_plural = u'Групповые заявки'

class GroupTicketAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'group', 'created', 'ticket_status', 'ticket_comment')
    list_filter = ['email', 'group', 'created', 'ticket_status']
    search_fields = ['email', ]
    date_hierarchy = 'created'
    fields = ('name', 'email', 'group', 'comment', 'sale', 'ticket_status', 'ticket_comment')
    form = TicketAdminForm

    def get_queryset(self, request):
        return self.model.objects.filter(sale=False, group__isnull=False)

    def suit_row_attributes(self, obj, request):
        css_class = {
            1: 'success',
            0: 'warning',
            2: 'error',
        }.get(obj.ticket_status)
        if css_class:
            return {'class': css_class, 'data': obj.name}

class Sale(Ticket):
    class Meta:
        proxy = True
        verbose_name = u'Продажа'
        verbose_name_plural = u'Продажи'


class SaleAdminForm(ModelForm):
    class Meta:
        widgets = {
            'price': EnclosedInput(append=u'руб.'),
            'commission': EnclosedInput(append=u'руб.'),
            'total_price': EnclosedInput(append=u'руб.'),
            'comment': AutosizedTextarea,
            'sale_comment': AutosizedTextarea,
        }


class SaleAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        return self.model.objects.filter(sale=True)

    def has_add_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        #if obj.price:
        #    obj.total_price = obj.price
        #    if obj.commission:
        #        obj.total_price = obj.price + obj.commission
        #    obj.save()
        if not obj.price:
            obj.price = 0
        if not obj.commission:
            obj.commission = 0
        obj.total_price = obj.price + obj.commission
        obj.save()
            

    def suit_row_attributes(self, obj, request):
        css_class = {
            2: 'success',
            1: 'warning',
            0: 'error',
        }.get(obj.sale_status)
        if css_class:
            return {'class': css_class, 'data': obj.name}

    list_display = ('name', 'email', 'group', 'price', 'commission', 'total_price', 'sale_status', 'sale_comment')
    list_filter = ['travel_start', 'sale_status', 'group', ]
    search_fields = ['email', ]
    date_hierarchy = 'travel_start'
    fields = ('name', 'email', 'group', 'comment', 'sale', 'sale_status', 'sale_comment', 'travel_start', 'travel_end', 'price', 'commission', 'total_price')
    form = SaleAdminForm


class SetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'email')

class SliderAdmin(admin.ModelAdmin):
    list_display = ('pic', )

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'pic', )

admin.site.register(Ticket, TicketAdmin)
admin.site.register(GroupTicket, GroupTicketAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Setup, SetupAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Avatar)
