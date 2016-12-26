# -*- coding: UTF-8 -*-
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse

from voiper.models import Context
from voiper.forms import ContextForm
from voiper.tables.context import ContextTable
from django_tables2 import SingleTableView


class ContextList(SingleTableView):
    # queryset = Context.objects.all()
    table_class = ContextTable
    model = Context
    # context_object_name = 'context'
    template_name = 'contexts/list.html'

    # def get_context_data(self, **kwargs):
    #     context = super(ContextList, self).get_context_data(**kwargs)
    #     context['table'] = ContextTable(Context.objects.all())
    #     return context


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
