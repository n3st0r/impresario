# -*- coding: UTF-8 -*-
from django.conf.urls import url
from voiper.views.numbers import NumberList, NumberEdit

# app_name = 'voipnumbers'


urlpatterns = [
    # dokładnie: /voip/number/
    url(r'^$', NumberList.as_view(), name='list'),

    # np.: /voip/number/1/
    url(r'^(?P<pk>\d+)/$', NumberEdit.as_view(), name='edit'),

]
