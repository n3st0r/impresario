# -*- coding: UTF-8 -*-
from django.conf.urls import url
from voiper.views.devices import DeviceList, DeviceAdd, DeviceEdit, DevCfgGenerator

app_name = 'voiper'

urlpatterns = [
    # dokładnie: /voip/device/
    url(r'^$', DeviceList.as_view(), name='voip_devices'),

    # dokładnie: /voip/device/add/
    url(r'^add/$', DeviceAdd.as_view(), name='voip_device_add'),

    # np.: /voip/device/1/
    url(r'^(?P<pk>\d+)/$', DeviceEdit.as_view(), name='voip_device_edit'),

    # np.: /voip/device/1/generator
    url(r'^(?P<pk>\d+)/generator/$', DevCfgGenerator.as_view(), name='generator'),
]
