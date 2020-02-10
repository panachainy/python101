from tweet.models import Tweet, User
from django.test import TestCase
from datetime import datetime


class Test_models(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            email='user1@user1.com'
        )
        self.user2 = User.objects.create(
            email='user2@user2.com'
        )
        Tweet.objects.create(
            body="test", is_retweet=False, author=self.user1, owner=self.user1)
        Tweet.objects.create(
            body="test2", is_retweet=False, author=self.user2, owner=self.user2)

    def test_tweet(self):
        qs = Tweet.objects.all()
        self.assertEqual(qs.count(), 2)
        tw1 = Tweet.objects.get(author=self.user1)
        tw2 = Tweet.objects.get(author=self.user2)
        self.assertEqual(tw1.body, "test")
        self.assertEqual(tw2.body, "test2")
