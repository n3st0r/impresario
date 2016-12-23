# -*- coding: UTF-8 -*-
from django import forms
from crispy_forms.helper import FormHelper
from impresario.models import Person, Customer


class PersonCreateForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = [
            'first_name',
            'last_name',
        ]


class CustomerForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    name = forms.CharField(
        label='Nazwa klienta',
        min_length=2,
        max_length=32,
    )
    # sip_proxy = forms.GenericIPAddressField(protocol='IPv4')

    class Meta:
        model = Customer
        fields = [
            'name',
            'contact',
            'sip_proxy',
            'logo_url',
        ]
