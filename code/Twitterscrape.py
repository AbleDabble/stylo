# Too get tweepy to import use:
# conda install -c conda-forge tweepy

# Then in anaconda package manager, make sure it includes the conda-forge channel
import tweepy
import io
import json


# Uses personal API keys to access, DONT FORGET TO CHANGE
with open('../config/config.json', 'r') as f:
    config = json.load(f)
config = config['twitter']

auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
auth.set_access_token(config['access_token'], config['access_token_secret'])
api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# Test list of users for multiple printings at a time
user_list = ["Username"]


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

class twitScrape():
    def getIndivTweets(self, username):
        path = '../corpora/twitter_corpus/'
        save_path = path + username + ".txt"
        save = ""
        count = 0
        usercheck = True

        try:
            timeline2 = api.user_timeline(screen_name=username, count=60, tweet_mode='extended')
            for tweets in timeline2:
                save += "\n\n"
                save += tweets.full_text
                count += 1
                if count >= 60:
                    break
                with io.open(save_path, "w", encoding="utf-8") as w:
                     w.write(save)
        except Exception:
            usercheck = False
            print("User " + username + " not found or Tweets don't exist")
            pass
        # add code here to work with GUI pop-up


scraper = twitScrape()
usrname = "shakira"
scraper.getIndivTweets(usrname)
print('No errors')
usernames = ["BarackObama", "justinbieber", "katyperry","TheEllenShow", "YouTube",
             "BillGates","CNN", "elonmusk", "BrunoMars", "realmadrid", "Harry_Styles",
             "TheTattedNative", "MountainWest", "1matree", "Markiplier", "pixlpit",
             "LordMinion777", "Twitch", "DeadByBHVR", "MatPatGT", "Jack_Septic_Eye",
             "taylorswift13", "Cristiano",  "YouTube", "jimmyfallon", "NASA",  "NBA",
             "Adele", "NFL", "ShawnMendes", "ActuallyNPH", "NatGeo",
             "TheEconomist", "danieltosh", "Google", "MariahCarey", "garyvee",
             "GuyKawasaki", "richardbranson", "ariannahuff", "tferriss", "TonyRobbins",
             "mcuban", "BillGates", "PatFlynn", "ericries", "TheSharkDaymond",
             "LizAnnSonders", "morganhousel", "DaveRamsey", "jimcramer", "WarrenBuffett",
             "TheRetailDoctor", "Shopify", "BarcodeAndrew", "beeemapp", "FierceRetail",
             "Walmart", "HomeDepot", "amazon", "Target", "BBYNews",
             "YouTubeGaming", "QuarterJade", "IGN", "Valkyrae", "peterparkTV"]


#THIS FUNCTION CREATES/UPDATES THE STARTING DATASET
#for user in usernames:
 #   scraper.getIndivTweets(user)



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
