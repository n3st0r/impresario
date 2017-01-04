# -*- coding: UTF-8 -*-
from django.conf.urls import url
from voiper.views.asterisk import CustomersView, CustomerSipView, StencilView, stencil_create

app_name = 'voip_asterisk'

urlpatterns = [
    # dokładnie: /voip/asterisk/
    url(r'^$', CustomersView.as_view(), name='list'),
    # dokładnie: /voip/asterisk/stencil/
    url(r'^stencil/$', StencilView.as_view(), name='stencil_list'),
    # url(r'^stencil/add/$', StencilCreate.as_view(), name='stencil_create'),
    url(r'^stencil/add/$', stencil_create, name='stencil_create'),

    url(r'^(?P<pk>\d+)/$', CustomerSipView.as_view(), name='sip_accounts')

]