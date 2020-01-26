from tweet.models import Tweet
from django.test import TestCase
from datetime import datetime

class Test_models(TestCase):
    def setUp(self):
        Tweet.objects.create(
            body="test", is_retweet=False, author="one_author", owner="one_owner")
        Tweet.objects.create(
            body="test2", is_retweet=False, author="two_author", owner="two_owner")

    def test_tweet(self):
        qs = Tweet.objects.all()
        self.assertEqual(qs.count(), 2)