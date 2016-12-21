# -*- coding: UTF-8 -*-
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse
from voiper.models import Number
from voiper.forms import NumberForm


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
        return reverse('voiper:voip_numbers')
