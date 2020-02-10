import pytest

from django.urls import reverse, resolve
from django.test import TestCase, Client, TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient


class Test_tweets(TestCase):

    def setUp(self):
        # arrange
        self.client = APIClient()
        self.user = User.objects.create_user('admin', 'example@example.com')
        self.client.force_authenticate(user=self.user)

    def test_tweets_unauth(self):
        # arrange
        self.client.force_authenticate(user=None)

        # action
        response = self.client.get('/tweets')

        # assert
        self.assertEqual(response.status_code,
                         401,
                         "The status code does not match.",)

    # def test_tweets_auth(self):
    #     # action
    #     response = self.client.get('/tweets', follow=True)

    #     # assert
    #     self.assertEqual(response.status_code, 200,
    #                      "The status code does not match.")


class Test_health(TestCase):
    def setUp(self):
        # arrange
        self.client = APIClient()
        self.user = User.objects.create_user('admin', 'example@example.com')
        self.client.force_authenticate(user=self.user)

    def test_health(self):
        # action
        response = self.client.get('/api/health', follow=True)

        # assert
        self.assertEqual(response.status_code, 200,
                         "The status code does not match.")

    def test_health_with_auth(self):
        # action
        response = self.client.get('/api/health_auth', follow=True)

        # assert
        self.assertEqual(response.status_code, 200,
                         "The status code does not match.")

    def test_health_with_unauth(self):
        # arrange
        self.client.force_authenticate(user=None)

        # action
        response = self.client.get('/api/health_auth', follow=True)

        # assert
        self.assertEqual(response.status_code, 401,
                         "The status code does not match.")
