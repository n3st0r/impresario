# -*- coding: UTF-8 -*-
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse

from voiper.models import Device
from voiper.forms import DeviceForm


class DeviceList(ListView):
    queryset = Device.objects.all()
    model = Device
    template_name = 'devices/list.html'


class DeviceAdd(CreateView):
    queryset = Device.objects.all()
    form_class = DeviceForm
    model = Device
    template_name = 'devices/edit.html'


class DeviceEdit(UpdateView):
    queryset = Device.objects.all()
    form_class = DeviceForm
    model = Device
    template_name = 'devices/edit.html'

    def get_success_url(self):
        return reverse('voiper:voip_devices')
