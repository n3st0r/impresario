# -*- coding: utf-8 -*-
"""
====================================================================
  Testy modeli danych aplikacji Impresario
====================================================================
"""

from django.test import TestCase
from impresario.models import Person
import crm.tools as tools


class TestImprasario(TestCase):

    def setUp(self):
        self.prepare_persons(True)

    def test_person(self):
        for data in self.persons:
            o_person = Person.objects.get(first_name=data[0])
            self.assertEqual(o_person.first_name, data[0])
            self.assertEqual(o_person.last_name, data[1])

    def prepare_persons(self, generate_fixtures=False):

        for dana in self.persons:
            o_person, junk = Person.objects.get_or_create(first_name=dana[0], last_name=dana[1])
            o_person.save()
        if generate_fixtures:
            tools.generate_fixtures(filename='persons.json', app='impresario.Person')

    persons = ['Johny', 'Walker']
