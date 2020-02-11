import pytest
from datetime import date

from django.urls import reverse, resolve
from django.test import TestCase, Client, TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from tweet.models import User as Tweet_user
from tweet.models import Tweet

import json


class Test_tweets(TestCase):

    def setUp(self):
        # arrange
        self.client = APIClient()

        # arrange User auth
        self.user = User.objects.create_user(
            username='adminTest', email='adminTest.ny@gmail.com')
        self.client.force_authenticate(user=self.user)

        # arrange User internal
        Tweet_user.objects.create(
            email='adminTest.ny@gmail.com'
        )
        Tweet_user.save

    def test_tweets_unauth(self):
        # arrange
        self.client.force_authenticate(user=None)

        # action
        response = self.client.get('/tweets')

        # assert
        self.assertEqual(response.status_code,
                         401,
                         "The status code does not match.",)

    def test_tweets_write(self):
        # arrange
        testUser = Tweet_user.objects.get(email='adminTest.ny@gmail.com')

        Tweet.objects.create(body="testBody1",
                             author=testUser,
                             owner=testUser,
                             created_at=date.today(),
                             updated_at=date.today())

        Tweet.objects.create(body="testBody2",
                             author=testUser,
                             owner=testUser,
                             created_at=date.today(),
                             updated_at=date.today())

        Tweet.objects.create(body="testBody3",
                             author=testUser,
                             owner=testUser,
                             created_at=date.today(),
                             updated_at=date.today())
        Tweet.save

        # action
        response = self.client.get('/tweets', follow=True)
        tweetDatas = json.loads(response.content)

        # assert
        self.assertEqual(response.status_code, 200,
                         "The status code does not match.")
        self.assertEqual(tweetDatas[0]["body"], "testBody1")
        self.assertEqual(tweetDatas[1]["body"], "testBody2")
        self.assertEqual(tweetDatas[2]["body"], "testBody3")
        self.assertEqual(len(tweetDatas), 3)


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
