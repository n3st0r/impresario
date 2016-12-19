# -*- coding: UTF-8 -*-
from django.conf.urls import url
from impresario.views import PersonList


app_name = 'impresario'

urlpatterns = [
    # example: /person/
    url(r'^$', PersonList.as_view(), name='persons_list'),

]