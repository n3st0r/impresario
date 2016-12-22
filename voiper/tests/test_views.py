import pytest
from django.core.urlresolvers import reverse
from voiper.views.devices import DeviceList
from django.test import TestCase, RequestFactory


def test_an_admin_view(admin_client):
    response = admin_client.get('/admin/')
    assert response.status_code == 200


def test_voip_devices_view(admin_client):
    url = reverse('voiper:voip_devices')
    assert url == '/voip/device/'
    response = admin_client.get(url)
    assert response.status_code == 200


# def test_voip_devices_list(RequestFactory):
#     request = RequestFactory.get('/customer/details')
#     response = DeviceList(request)
#     assert response.status_code == 200
