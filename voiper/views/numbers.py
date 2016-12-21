# -*- coding: UTF-8 -*-
from django.views.generic import ListView, CreateView, UpdateView
from voiper.models import Number


class NumberList(ListView):
    queryset = Number.objects.all()
    model = Number
    template_name = 'numbers/list.html'
