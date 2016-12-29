# -*- coding: UTF-8 -*-
from django.conf.urls import url
from impresario.views import PersonList2, PersonAdd, PersonEdit, PersonList2Json,CustomerList, CustomerAdd, CustomerEdit


app_name = 'impresario'

urlpatterns = [
    # exactly: /impresario/person/
    url(r'^contact/$', PersonList2.as_view(), name='persons_list'),

    url(r'^persons_data/$', PersonList2Json.as_view(), name="persons_list_json"),

    # exactly: /impresario/person/add
    url(r'^contact/add/$', PersonAdd.as_view(), name='persons_add'),

    # example: /impresario/person/1
    url(r'^contact/(?P<pk>\d+)/$', PersonEdit.as_view(), name='persons_edit'),

    # example: /impresario/
    url(r'^$', CustomerList.as_view(), name='customer_list'),

    # exactly: /impresario/add
    url(r'^add/$', CustomerAdd.as_view(), name='customer_add'),

    # example: /impresario/1
    url(r'^(?P<pk>\d+)/$', CustomerEdit.as_view(), name='customer_edit'),

]