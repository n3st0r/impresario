# -*- coding: UTF-8 -*-
from django.conf.urls import url
from voiper.views.contracts import ContractList, ContractAdd, ContractEdit

app_name = 'voip_contract'

urlpatterns = [
    # dokładnie: /voip/contract/
    url(r'^$', ContractList.as_view(), name='list'),

    # dokładnie: /voip/contract/add/
    url(r'^add/$', ContractAdd.as_view(), name='add'),

    # np.: /voip/contract/1/
    url(r'^(?P<pk>\d+)/$', ContractEdit.as_view(), name='edit'),

]
