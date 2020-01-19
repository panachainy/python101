from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tweet.models import Tweet
from tweet.serializers import TweetSerializer
from tweet.tweetmanament import TweetManagement

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

@api_view(['GET', 'POST'])
def tweet_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TweetSerializer(data=request.data["tweet"])
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

@api_view(['POST','PUT','DELETE'])
def tweet_retweet(request, id, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        tweet = Tweet.objects.get(pk=id)
    except Tweet.DoesNotExist:
        return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    if request.method == 'PUT':
        serializer = TweetSerializer(tweet,data=request.data["tweet"])
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST':
        data = request.data["tweet"]
        data["is_retweet"] = True
        serializer = TweetSerializer(data=data)
        
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
