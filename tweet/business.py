from tweet.serializers import TweetSerializer


class TweetManagement:

    # Copy tweet and set is_retweet is True
    def retweet_new(self, old_data, request_tweet_data):
        data = request_tweet_data
        data["is_retweet"] = True
        data["author"] = old_data.author_id
        data["owner"] = old_data.owner_id
        return TweetSerializer(data=data)

    # Set owner and author for tweet
    def set_tweet_owner(self, tweet, user):
        tweet['author'] = user.id
        tweet['owner'] = user.id
        return tweet
