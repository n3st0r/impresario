from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory

from impresario.views import PersonList, PersonAdd


class SimpleTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_list(self):
        request = self.factory.get('/impresario/')
        request.user = AnonymousUser()
        response = PersonList.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_details(self):
        request = self.factory.get('/impresario/1/')
        request.user = AnonymousUser()
        response = PersonAdd.as_view()(request)
        self.assertEqual(response.status_code, 200)
