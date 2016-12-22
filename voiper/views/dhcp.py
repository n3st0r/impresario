# -*- coding: UTF-8 -*-
from django.views.generic import TemplateView


class DhcpView(TemplateView):
    template_name = 'dhcp/view.html'
