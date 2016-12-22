# -*- coding: UTF-8 -*-
from django.conf.urls import url
from voiper.views.dhcp import DhcpView

# app_name = 'voiper'

urlpatterns = [
    # dokładnie: /voip/dhcp/
    url(r'^$', DhcpView.as_view(), name='view'),


]
