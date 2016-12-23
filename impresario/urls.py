# -*- coding: UTF-8 -*-
from django.conf.urls import url
from impresario.views import PersonList, PersonAdd, PersonEdit, CustomerList, CustomerAdd


app_name = 'impresario'

urlpatterns = [
    # example: /person/
    url(r'^contact/$', PersonList.as_view(), name='persons_list'),

    # example: /person/add
    url(r'^contact/add/$', PersonAdd.as_view(), name='persons_add'),

    # example: /person/add
    url(r'^contact/(?P<pk>\d+)/$', PersonEdit.as_view(), name='persons_edit'),

    # example: /impresario/customer/
    url(r'^$', CustomerList.as_view(), name='customer_list'),

    # exactly: /impresario/customer/add
    url(r'^add/$', CustomerAdd.as_view(), name='customer_add'),

]