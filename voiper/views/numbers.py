# -*- coding: UTF-8 -*-
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse
from voiper.models import Number
from voiper.forms import NumberForm
from voiper.services.security import gen_password


class NumberList(ListView):
    queryset = Number.objects.all()
    model = Number
    template_name = 'numbers/list.html'


class NumberEdit(UpdateView):
    form_class = NumberForm
    queryset = Number.objects.all()
    model = Number
    template_name = 'numbers/edit.html'

    def get_success_url(self):
        return reverse('voip_numbers:list')


class NumberAdd(CreateView):
    form_class = NumberForm
    model = Number
    template_name = 'numbers/edit.html'

    def get_initial(self):
        return {'secret': gen_password()}

    def get_success_url(self):
        return reverse('voip_numbers:list')
