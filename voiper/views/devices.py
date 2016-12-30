# -*- coding: UTF-8 -*-
from django.views.generic import ListView, CreateView, UpdateView, View
from django.core.urlresolvers import reverse

from voiper.models import Device, Contract
from impresario.models import Customer
from voiper.forms import DeviceForm
from voiper.services.generator import generate_config


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
        context['link'] = reverse('voiper:generator', kwargs={'pk': context['dev'].pk})
        # !!!!!!!!!!!!!!!! POPRAWIC !!!!!!!!!!!!!!!!!!!!!!!!
        context['customer'] = Customer.objects.get(pk=1)
        if context['contracts']:
            context['config'] = generate_config(
                contracts=context['contracts'],
                customer=context['customer'],
                option=context['dev'].get_option(),
            )
        context['submit_text'] = 'Aktualizuj parametry urządzenia'
        return context


class DevCfgGenerator(View):
    template_name = 'devices/edit.html'

    def dispatch(self, request, *args, **kwargs):
        dev = Device.objects.get(pk=self.kwargs['pk'])
        contracts = Contract.objects.filter(id_device=self.kwargs['pk']).select_related('id_number__id_customer')
        customer = Customer.objects.get(pk=1)
        generate_config(
            contracts=contracts,
            customer=customer,
            option=dev.get_option(),
            save=True
        )
        return DeviceList.as_view()(request, *args, **kwargs)
