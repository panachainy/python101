from rest_framework import serializers
from tweet.models import Tweet

class TweetSerializer(serializers.Serializer):
    body = serializers.CharField(max_length=100,required=None)
    author = serializers.CharField(max_length=100,required=None)
    owner = serializers.CharField(max_length=100,required=None)
    is_retweet = serializers.BooleanField(default=False)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Tweet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance = validated_data.get('id', instance.id)
        instance.body = validated_data.get('code', instance.code)
        instance.save()
        return instance

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['body','is_retweet']

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Tweet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance = validated_data.get('id', instance.id)
        instance.body = validated_data.get('code', instance.code)
        instance.save()
        return instance