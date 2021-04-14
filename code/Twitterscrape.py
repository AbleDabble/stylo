# Too get tweepy to import use:
# conda install -c conda-forge tweepy

# Then in anaconda package manager, make sure it includes the conda-forge channel
import tweepy
import io

# Uses personal API keys to access, DONT FORGET TO CHANGE
# BEFORE PUSHING!!
consumer_key = 'xwMMqenNbrbUZlRQZfmsnovCN'
consumer_secret = '7C0cWCPiLcB31n5BL2wFziUNeFwbhShNOroE8q0MS3JedDVKu8'

access_token = '1227390177317965825-WivPuwRbbW5OObwkTBkFBlI1PSpd9i'
access_token_secret = 'RjU5SMSiznkNTe6fYpvxdCwZ4W8OvB5cAjSSE09MXo9n1'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# Test list of users for multiple printings at a time
user_list = ["TheEpic_Ace", "MountainWest", "markiplier"]


# create a stream listener

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False


def streamTweet():
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(track=['python'])


# This Function is for adding individual users to the corpus!
def getIndivTweets(username):
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


usernames = ["BarackObama", "justinbieber", "katyperry","TheEllenShow", "YouTube",
             "BillGates","CNN", "elonmusk", "BrunoMars", "realmadrid", "Harry_Styles"]

for user in usernames:
    getIndivTweets(user)
# user = "TheEpic_Ace"
# getIndivTweets(user)
# streamTweet()

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
