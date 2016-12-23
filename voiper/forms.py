# -*- coding: UTF-8 -*-
from django import forms
from crispy_forms.helper import FormHelper
from voiper.models import Device, Number


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = [
            'mac',
            'ip',
            'dev',
        ]


class NumberForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    secret = forms.CharField(
        label='Hasło dla linii',
        min_length=20,
        max_length=32,
    )
    number = forms.CharField(
        label='Numer linii',
        min_length=9,
        max_length=9,
    )
    aster_template = forms.Textarea()

    class Meta:
        model = Number
        fields = [
            'number',
            'secret',
            'id_customer',
            'id_context',
            'aster_template',
        ]
