# -*- coding: UTF-8 -*-
from django.conf.urls import url
from voiper.views.contexts import ContextList, ContextAdd, ContextEdit

app_name = 'voip_context'

urlpatterns = [
    # dokładnie: /voip/context/
    url(r'^$', ContextList.as_view(), name='list'),

    # dokładnie: /context/add/
    url(r'^add/$', ContextAdd.as_view(), name='add'),

    # np.: /context/1/
    url(r'^(?P<pk>\d+)/$', ContextEdit.as_view(), name='edit'),

]
