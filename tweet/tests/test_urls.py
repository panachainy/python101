import pytest
from django.urls import reverse, resolve
from django.test import TestCase, Client, TestCase


class Test_urls(TestCase):

    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_tweets_unauth(self):
        response = self.client.get('/tweets')
        self.assertEqual(response.status_code, 401)
