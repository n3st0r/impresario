# -*- coding: UTF-8 -*-
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse

from voiper.models import Device, Contract
from impresario.models import Customer
from voiper.forms import DeviceForm
from voiper.services.generator import generate_config_c7940


class DeviceList(ListView):
    queryset = Device.objects.all()
    model = Device
    template_name = 'devices/list.html'


class DeviceAdd(CreateView):
    form_class = DeviceForm
    model = Device
    template_name = 'devices/edit.html'

    def get_context_data(self, **kwargs):
        context = super(DeviceAdd, self).get_context_data(**kwargs)
        context['submit_text'] = 'Dodaj urządzenie'
        return context


class DeviceEdit(UpdateView):
    form_class = DeviceForm
    model = Device
    template_name = 'devices/edit.html'
    context_object_name = 'dev'

    def get_success_url(self):
        return reverse('voiper:voip_devices')

    def get_context_data(self, **kwargs):
        context = super(DeviceEdit, self).get_context_data(**kwargs)
        context['contracts'] = Contract.objects.filter(id_device=context['dev']).select_related('id_number__id_customer')
        context['filename'] = context['dev'].config_filename
        context['customer'] = Customer.objects.get(pk=1)
        if context['contracts']:
            context['config'] = generate_config_c7940(
                contracts=context['contracts'],
                customer=context['customer']
            )
        context['submit_text'] = 'Aktualizuj parametry urządzenia'
        return context
