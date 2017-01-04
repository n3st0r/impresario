# -*- coding: UTF-8 -*-
from django import forms
from crispy_forms.helper import FormHelper
from voiper.models import Context, Contract, Device, Number, Stencil


class ContextForm(forms.ModelForm):
    class Meta:
        model = Context
        fields = [
            'name',
            'description',
        ]


class ContractForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False

    class Meta:
        model = Contract
        fields = [
            'id_number',
            'id_device',
            'device_line',
        ]


class StencilForm(forms.ModelForm):
    class Meta:
        model = Stencil
        fields = ('name', 'description', 'content', )


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

    secretary_number = forms.ModelChoiceField(
        queryset=Number.objects.all(),
        required=False,
        help_text="Jeśli przyjście ma być kierowane na inny numer, to tutaj go wybierz.")

    class Meta:
        model = Number
        fields = [
            'number',
            'secret',
            'id_customer',
            'id_context',
            'stencil',
            'aster_template',
            'secretary',
            'secretary_number',
        ]
