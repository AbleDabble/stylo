# Too get tweepy to import use:
# conda install -c conda-forge tweepy

# Then in anaconda package manager, make sure it includes the conda-forge channel
import tweepy
import io

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


# This Function is for adding individual users to the corpus!
def getTweets(username):
    path = '../corpora/twitter_corpus/'
    save_path = path + username + ".txt"
    save = ""
    count = 0

    timeline2 = api.user_timeline(screen_name=username, count=60, tweet_mode='extended')
    for tweets in timeline2:
        save += "\n\n"
        save += tweets.full_text
        count += 1
        if count >= 60:
            break
        with io.open(save_path, "w", encoding="utf-8") as w:
            w.write(save)

    # print(username)
    # print(tweets.full_text)
    # print("\n")


user = "TheEpic_Ace"
getTweets(user)

# for user in user_list:
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
