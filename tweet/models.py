from django.db import models
from datetime import datetime

class Tweet(models.Model):
    id = models.IntegerField(primary_key=True)
    body = models.CharField(max_length=50)
    # author = models.CharField(max_length=50)
    # owner = models.CharField()
    is_retweet = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)
    class Meta:
        ordering = ['id']


# class User(models.Model):
#     id = models.IntegerField(primary_key=True)
#     email = models.CharField()
#     password = models.CharField()
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
