# -*- coding: UTF-8 -*-
from django.views.generic import ListView, CreateView, UpdateView
from impresario.models import Person, Customer
from impresario.forms import PersonCreateForm, CustomerForm
from django.core.urlresolvers import reverse
from django_datatables_view.base_datatable_view import BaseDatatableView


class PersonList(ListView):
    queryset = Person.objects.all()
    model = Person
    template_name = 'persons/list.html'


class PersonList2(ListView):
    queryset = Person.objects.all()
    model = Person
    template_name = 'persons/list2.html'


class PersonList2Json(BaseDatatableView):
    model = Person
    columns = ['last_name', 'first_name']
    order_columns = ['last_name', 'first_name']


class PersonAdd(CreateView):
    model = Person
    template_name = 'persons/form.html'
    form_class = PersonCreateForm

    def get_success_url(self):
        return reverse('impresario:persons_list')


class PersonEdit(UpdateView):
    model = Person
    template_name = 'persons/form.html'
    form_class = PersonCreateForm

    def get_success_url(self):
        return reverse('impresario:persons_list')


class CustomerList(ListView):
    queryset = Customer.objects.all()
    model = Customer
    template_name = 'customers/list.html'


class CustomerAdd(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/form.html'

    def get_success_url(self):
        return reverse('impresario:customer_list')


class CustomerEdit(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/form.html'

    def get_success_url(self):
        return reverse('impresario:customer_list')
