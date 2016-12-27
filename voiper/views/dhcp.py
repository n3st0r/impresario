# -*- coding: UTF-8 -*-
from django.views.generic import TemplateView
from voiper.services.dhcp import generate_config
from voiper.services.generator import generate_config_c7940


class DhcpView(TemplateView):
    template_name = 'dhcp/view.html'

    def get_context_data(self, **kwargs):
        context = super(DhcpView, self).get_context_data(**kwargs)
        context['dhcp_file'] = generate_config()
        # context['c7940'] = generate_config_c7940()
        return context
