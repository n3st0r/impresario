# -*- coding: UTF-8 -*-
from django.conf.urls import url
from voiper.views.devices import DeviceList, DeviceAdd, DeviceEdit

app_name = 'service'

urlpatterns = [
    # dokładnie: /device/
    url(r'^$', DeviceList.as_view(), name='voip_devices'),

    # dokładnie: /device/add/
    url(r'^add/$', DeviceAdd.as_view(), name='voip_device_add'),

    # np.: /device/1/
    url(r'^(?P<pk>\d+)/$', DeviceEdit.as_view(), name='voip_device_edit'),

]
