# -*- coding: UTF-8 -*-
from django.conf.urls import url
from voiper.views.sip import CustomersView, CustomerSipView

app_name = 'voip_sip'

urlpatterns = [
    # dokładnie: /voip/sip/
    url(r'^$', CustomersView.as_view(), name='list'),

    url(r'^(?P<pk>\d+)/$', CustomerSipView.as_view(), name='sip_accounts')

]