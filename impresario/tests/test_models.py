# -*- coding: utf-8 -*-
"""
====================================================================
  Testy modeli danych aplikacji Impresario
====================================================================
"""

from django.test import TestCase
from impresario.models import Person
import crm.tools as tools
import json


class TestImprasario(TestCase):
    fixtures = ['persons.json', ]

    def test_person(self):
        with open("impresario/fixtures/persons.json") as file:
            json_data = json.load(file)
            file.close()
            for data in json_data:
                o_person = Person.objects.get(pk=data['pk'])
                self.assertEqual(o_person.first_name, data['fields']['first_name'])
                self.assertEqual(o_person.last_name, data['fields']['last_name'])
