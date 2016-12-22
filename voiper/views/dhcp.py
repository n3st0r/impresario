# -*- coding: UTF-8 -*-
from django.views.generic import TemplateView
from voiper.services.dhcp import generate_config


class DhcpView(TemplateView):
    template_name = 'dhcp/view.html'

    def get_context_data(self, **kwargs):
        context = super(DhcpView, self).get_context_data(**kwargs)
        context['dhcp_file'] = generate_config()
        return context
