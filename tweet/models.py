from django.db import models
from datetime import datetime


class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)


class Tweet(models.Model):
    id = models.AutoField(primary_key=True)
    body = models.CharField(max_length=100, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tweet_author_user')
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tweet_owner_user')
    is_retweet = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ['id']
