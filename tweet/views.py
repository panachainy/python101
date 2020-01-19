from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from tweet.models import Tweet
from tweet.serializers import TweetSerializer
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def tweet_list(request, format=None):
    if request.method == 'GET':
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TweetSerializer(data=request.data["tweet"])
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def tweet_detail(request, pk, format=None):

    try:
        tweet = Tweet.objects.get(pk=pk)
    except Tweet.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        serializer = TweetSerializer(tweet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TweetSerializer(tweet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)