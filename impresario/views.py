# -*- coding: UTF-8 -*-
from django.views.generic import ListView, CreateView, UpdateView
from impresario.models import Person
from impresario.forms import PersonCreateForm
from django.core.urlresolvers import reverse


class PersonList(ListView):
    queryset = Person.objects.all()
    model = Person
    template_name = 'persons_list.html'


class PersonAdd(CreateView):
    model = Person
    template_name = 'person_form.html'
    form_class = PersonCreateForm

    def get_success_url(self):
        return reverse('impresario:persons_list')


class PersonEdit(UpdateView):
    model = Person
    template_name = 'person_form.html'
    form_class = PersonCreateForm

    def get_success_url(self):
        return reverse('impresario:persons_list')
