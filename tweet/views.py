from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from tweet.models import Tweet,User
from tweet.serializers import TweetSerializer,UserSerializer
from rest_framework.permissions import IsAuthenticated
from tweet.business import TweetManagement


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def tweet_list(request, id=None, format=None):
    if request.method == 'GET':
        user_data = User.objects.get(email=request.user.email)

        if id is not None:
            tweet = Tweet.objects.get(pk=id)
            if tweet.owner.email != user_data.email:
                return Response("Unauthorize this content",status.HTTP_401_UNAUTHORIZED)
            serializer = TweetSerializer(tweet)
        else:
            tweets = Tweet.objects.all().filter(owner=user_data.id)
            serializer = TweetSerializer(tweets, many=True)
            response_data = serializer.data
        return Response(response_data)

    elif request.method == 'POST':
        user_data = User.objects.get(email=request.user.email)
        tweet_manage = TweetManagement()
        data = tweet_manage.set_tweet_owner(request.data["tweet"],user_data)
        serializer = TweetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response_data = serializer.data
            response_data['owner'] = user_data.email
            response_data['author'] = user_data.email
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


@api_view(['POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def tweet_retweet(request, id, format=None):
    try:
        user_data = User.objects.get(email=request.user.email)
        tweet = Tweet.objects.get(pk=id)
        if tweet.owner.email != user_data.email:
            return Response("Unauthorize this content",status.HTTP_401_UNAUTHORIZED)
    except Tweet.DoesNotExist:
        return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    if request.method == 'PUT':
        tweet_manage = TweetManagement()
        data = tweet_manage.set_tweet_owner(request.data["tweet"],user_data)
        serializer = TweetSerializer(tweet,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST':
        tweet_manage = TweetManagement()
        serializer = tweet_manage.retweet_new(tweet,request.data["tweet"])
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            tweet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
