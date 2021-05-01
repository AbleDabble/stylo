# Too get tweepy to import use:
# conda install -c conda-forge tweepy

# Then in anaconda package manager, make sure it includes the conda-forge channel
import tweepy
import io
import json
import re

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

def remove_url(comment):
    return re.sub('(https?://)?(([a-zA-Z0-9]+)\.)+[a-zA-Z]{2,}(/[a-zA-Z0-9;/+\-%@,!^*&?:}{_=\\\]+)?(\.[a-zA-Z]+)?',
                  'url', comment)


# This Function is for adding individual users to the corpus!

class twitScrape():
    def getIndivTweets(self, username):
        path = '../corpora/twitter_corpus/'
        save_path = path + username + ".txt"
        save = ""
        count = 0
        usercheck = True

        try:
            timeline = api.user_timeline(screen_name=username, count=50, tweet_mode='extended')
            user_tweets = ''
            while len(user_tweets) < 240 * 50:
                if len(timeline) == 0:
                    print('not enough tweets')
                    return -1
                for tweet in timeline:
                    user_tweets += remove_url(tweet.full_text + ' ')
                    last_tweet = tweet.id - 1
                timeline = api.user_timeline(screen_name=username, count=50, tweet_mode='extended', max_id=last_tweet)
            with io.open(save_path, 'w', encoding='utf-8') as w:
                w.write(user_tweets[:240:50])
            return
        except:
            print('Failed to find user')
            return -1
                    
'''

        try:
            timeline2 = api.user_timeline(screen_name=username, count=50, tweet_mode='extended')
            all_tweets = ''
            while len(all_tweets) < 250 * 50:
                for tweets in timeline2:
                    all_tweets += tweets.full_text
                    all_tweets += '\n\n'
                    all_tweets = remove_url(all_tweets)

                #save += tweets.full_text
                if count >= 60:
                    break
            with io.open(save_path, "w", encoding="utf-8") as w:
                w.write(all_tweets[:240*50])
        except:
            usercheck = False
            print("User " + username + " not found or Tweets don't exist")
            return -1
        # add code here to work with GUI pop-up

usernames = ["BarackObama", "justinbieber", "katyperry", "TheEllenShow", "YouTube",
             "BillGates", "CNN", "elonmusk", "BrunoMars", "realmadrid", "Harry_Styles",
             "TheTattedNative", "MountainWest", "1matree", "Markiplier", "pixlpit",
             "LordMinion777", "Twitch", "DeadByBHVR", "MatPatGT", "Jack_Septic_Eye",
             "taylorswift13", "Cristiano", "YouTube", "jimmyfallon", "NASA", "NBA",
             "Adele", "NFL", "ShawnMendes", "ActuallyNPH", "NatGeo",
             "TheEconomist", "danieltosh", "Google", "MariahCarey", "garyvee",
             "GuyKawasaki", "richardbranson", "ariannahuff", "tferriss", "TonyRobbins",
             "mcuban", "BillGates", "PatFlynn", "ericries", "TheSharkDaymond",
             "LizAnnSonders", "morganhousel", "DaveRamsey", "jimcramer", "WarrenBuffett",
             "TheRetailDoctor", "Shopify", "BarcodeAndrew", "beeemapp", "FierceRetail",
             "Walmart", "HomeDepot", "amazon", "Target", "BBYNews",
             "YouTubeGaming", "QuarterJade", "IGN", "Valkyrae", "peterparkTV", "TheEpic_Ace"]


testData = ["MountainWest", "1matree", "Markiplier", "pixlpit",
             "LordMinion777", "Twitch", "DeadByBHVR", "MatPatGT", "Jack_Septic_Eye",
             "taylorswift13", "Cristiano", "YouTube", "jimmyfallon", "NASA", "NBA"]

# THIS FUNCTION CREATES/UPDATES THE STARTING DATASET
#for user in usernames:
 #   scraper.getIndivTweets(user)

'''
