# -*- coding: UTF-8 -*-
from django import forms
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
    class Meta:
        model = Number
        fields = [
            'number',
            'secret',
            'id_customer',
            'id_context',
        ]
