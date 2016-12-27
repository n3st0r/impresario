# -*- coding: UTF-8 -*-
from django.views.generic import CreateView, UpdateView
from django.core.urlresolvers import reverse

from voiper.models import Contract
from voiper.forms import ContractForm
from voiper.tables.contract import ContractTable
from django_tables2 import SingleTableView


class ContractList(SingleTableView):
    queryset = Contract.objects.select_related('id_device', 'id_number')
    table_class = ContractTable
    model = Contract
    paginate_by = 10
    template_name = 'contracts/list.html'


class ContractAdd(CreateView):
    form_class = ContractForm
    model = Contract
    template_name = 'contracts/form.html'

    def get_success_url(self):
        return reverse('voip_contract:list')


class ContractEdit(UpdateView):
    form_class = ContractForm
    model = Contract
    template_name = 'contracts/form.html'

    def get_success_url(self):
        return reverse('voip_contract:list')
