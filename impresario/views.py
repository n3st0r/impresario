# -*- coding: UTF-8 -*-
# from django.shortcuts import render
from django.views.generic import ListView
from impresario.models import Person


class PersonList(ListView):
    queryset = Person.objects.all()
    model = Person
    template_name = 'persons_list.html'
