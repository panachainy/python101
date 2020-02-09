from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from tweet.models import Tweet, User
from rest_framework.permissions import IsAuthenticated
from tweet.business import TweetManagement
from tweet.serializers import TweetSerializer


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def tweet_list(request, id=None, format=None):
    user_data = User.objects.get(email=request.user.email)
    if request.method == 'GET':
        if id is not None:
            tweet = get_tweet_by(id)
            if tweet.owner.email != user_data.email:
                return Response("Unauthorize this content", status.HTTP_401_UNAUTHORIZED)
            serializer = TweetSerializer(tweet)
            response_data = serializer.data
        else:
            tweets = Tweet.objects.all().filter(owner=user_data.id)
            serializer = TweetSerializer(tweets, many=True)
            response_data = serializer.data
        return Response(response_data)

    elif request.method == 'POST':
        tweet_manage = TweetManagement()
        data = tweet_manage.set_tweet_owner(request.data["tweet"], user_data)
        serializer = TweetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response_data = serializer.data
            response_data['owner'] = user_data.email
            response_data['author'] = user_data.email
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    elif request.method == 'PUT':
        tweet = get_tweet_by(id)
        tweet_manage = TweetManagement()
        data = tweet_manage.set_tweet_owner(request.data["tweet"], user_data)
        serializer = TweetSerializer(tweet, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            tweet = get_tweet_by(id)
            tweet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)


def get_tweet_by(id):
    if id is not None:
        return Tweet.objects.get(pk=id)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def tweet_retweet(request, id, format=None):
    try:
        tweet = Tweet.objects.get(pk=id)
    except Tweet.DoesNotExist:
        return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    if request.method == 'POST':
        tweet_manage = TweetManagement()
        serializer = tweet_manage.retweet_new(tweet, request.data["tweet"])
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
