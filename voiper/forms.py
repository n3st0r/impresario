# -*- coding: UTF-8 -*-
from django import forms
from voiper.models import Device


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = [
            'mac',
            'ip',
            'dev',
        ]
