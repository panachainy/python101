from rest_framework import serializers
from tweet.models import Tweet,User

class UserSerializer(serializers.ModelSerializer):
    #email = serializers.CharField(max_length=100,required=None)
    #password = serializers.CharField(max_length=100,required=None)

    class Meta:
        model = User
        fields = ['id','email','password','created_at','updated_at']

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data["email"]
        instance.password = validated_data["password"]
        instance.save()
        return instance

class TweetSerializer(serializers.ModelSerializer):
    #body = serializers.CharField(max_length=100,required=None)
    #is_retweet = serializers.BooleanField(default=False)

    class Meta:
        model = Tweet
        fields = ['id','body','is_retweet','owner','author','created_at','updated_at']

    def create(self, validated_data):
        """
        Create and return a new `Tweet` instance, given the validated data.
        """
        return Tweet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Tweet` instance, given the validated data.
        """
        instance.body = validated_data["body"]
        instance.owner = validated_data["owner"]
        instance.author = validated_data["author"]
        instance.save()
        return instance