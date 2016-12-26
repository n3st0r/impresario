# -*- coding: UTF-8 -*-
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django_tables2 import SingleTableView
from voiper.models import Number
from voiper.forms import NumberForm
from voiper.tables.numbers import NumberTable
from voiper.services.security import gen_password
from voiper.services.dialplan import create_sip_account


class NumberList(SingleTableView):
    # queryset = Number.objects.all()
    queryset = Number.objects.select_related('id_customer', 'id_context')
    table_class = NumberTable
    model = Number
    paginate_by = 10
    template_name = 'numbers/list.html'

    def get_context_data(self, **kwargs):
        context = super(NumberList, self).get_context_data(**kwargs)

        return context


class NumberListOld(ListView):
    queryset = Number.objects.all()
    model = Number
    template_name = 'numbers/list.html'


class NumberAdd(CreateView):
    form_class = NumberForm
    model = Number
    template_name = 'numbers/edit.html'

    def get_initial(self):
        return {'secret': gen_password()}

    def get_success_url(self):
        return reverse('voip_numbers:list')


class NumberEdit(UpdateView):
    form_class = NumberForm
    queryset = Number.objects.all()
    model = Number
    template_name = 'numbers/edit.html'
    context_object_name = 'number'

    def get_success_url(self):
        return reverse('voip_numbers:list')

    def get_context_data(self, **kwargs):
        context = super(NumberEdit, self).get_context_data(**kwargs)

        if context['number'].aster_template:
            context['sip_account'] = create_sip_account(context['number'])

        return context

    def get_initial(self, **kwargs):
        try:
            secretary_id = Number.objects.get(number=self.object.secretary_number)
            return {'secretary_number': secretary_id}
        except ObjectDoesNotExist:
            return {'secretary_number': ''}
