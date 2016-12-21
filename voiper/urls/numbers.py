# -*- coding: UTF-8 -*-
from django.conf.urls import url
from voiper.views.numbers import NumberList

app_name = 'voiper'


urlpatterns = [
    # dokładnie: /voip/number/
    url(r'^$', NumberList.as_view(), name='voip_numbers'),

]
