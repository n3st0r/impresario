# -*- coding: UTF-8 -*-
from django.conf.urls import url
from impresario.views import PersonList, PersonAdd


app_name = 'impresario'

urlpatterns = [
    # example: /person/
    url(r'^$', PersonList.as_view(), name='persons_list'),

    # example: /person/add
    url(r'^add/$', PersonAdd.as_view(), name='persons_add'),

]