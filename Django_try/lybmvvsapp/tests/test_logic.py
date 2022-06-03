import requests
from django.test import TestCase, Client
from django.urls import reverse

client = Client()
class TestViews(TestCase):
    def test_create(self):
        response = self.client.get(reverse('create'))
        self.assertEqual(response.status_code, 200)
