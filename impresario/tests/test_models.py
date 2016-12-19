# -*- coding: utf-8 -*-
"""
====================================================================
  Testy modeli danych aplikacji Impresario
====================================================================
"""

from django.test import TestCase
from impresario.models import Person


class TestImprasario(TestCase):
    contacts = ['Johny', 'Walker']

    def setUp(self):
        for dana in self.contacts:
            o_person, junk = Person.objects.get_or_create(first_name=dana[0], last_name=dana[1])
            o_person.save()

    def test_person(self):
        for data in self.contacts:
            o_person = Person.objects.get(first_name=data[0])
            self.assertEqual(o_person.first_name, data[0])
