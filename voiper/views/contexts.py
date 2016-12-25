# -*- coding: UTF-8 -*-
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse

from voiper.models import Context
from voiper.forms import ContextForm


class ContextList(ListView):
    queryset = Context.objects.all()
    model = Context
    template_name = 'contexts/list.html'


class ContextAdd(CreateView):
    form_class = ContextForm
    model = Context
    template_name = 'contexts/edit.html'

    def get_success_url(self):
        return reverse('voip_context:list')


class ContextEdit(UpdateView):
    form_class = ContextForm
    model = Context
    template_name = 'contexts/form.html'
    context_object_name = 'context'

    def get_success_url(self):
        return reverse('voip_context:list')
