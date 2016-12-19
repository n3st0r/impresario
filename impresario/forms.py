# -*- coding: UTF-8 -*-
from django import forms
from impresario.models import Person


class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name')
