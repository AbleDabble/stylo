# Too get tweepy to import use:
# conda install -c conda-forge tweepy

# Then in anaconda package manager, make sure it includes the conda-forge channel
import tweepy

# Uses personal API keys to access, DONT FORGET TO CHANGE
# BEFORE PUSHING!!
consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# Test list of users for multiple printings at a time
user_list = ["TheEpic_Ace", "MountainWest", "markiplier"]


def getTweets(username):
    timeline2 = api.user_timeline(screen_name=username, count=5, tweet_mode = 'extended')
    for tweets in timeline2:
        print(username)
        print(tweets.full_text)
        print("\n")

user = "TheEpic_Ace"
getTweets(user)


#for user in user_list:
#    user_id = user
#    timeline1 = api.user_timeline(screen_name=user_id, count=5, tweet_mode='extended')
#    for tweet in timeline1:
#        print(user_id)
#        print(tweet.full_text)
#        print("\n")

# timeline = api.user_timeline(screen_name=user_id, count=5, tweet_mode='extended')
# for tweet in timeline:
#    print(user_id)
#    print(tweet.full_text)
#    print("\n")
