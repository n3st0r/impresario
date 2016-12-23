# -*- coding: UTF-8 -*-
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse

from voiper.models import Device, Contract
from voiper.forms import DeviceForm
from voiper.services.generator import generate_config_c7940


class DeviceList(ListView):
    queryset = Device.objects.all()
    model = Device
    template_name = 'devices/list.html'


class DeviceAdd(CreateView):
    # queryset = Device.objects.all()
    form_class = DeviceForm
    model = Device
    template_name = 'devices/edit.html'


class DeviceEdit(UpdateView):
    form_class = DeviceForm
    model = Device
    template_name = 'devices/edit.html'
    context_object_name = 'dev'

    def get_success_url(self):
        return reverse('voiper:voip_devices')

    def get_context_data(self, **kwargs):
        context = super(DeviceEdit, self).get_context_data(**kwargs)
        context['service'] = Contract.objects.filter(id_device=context['dev']).select_related('id_number')
        context['filename'] = context['dev'].config_filename
        context['config'] = generate_config_c7940()
        return context
