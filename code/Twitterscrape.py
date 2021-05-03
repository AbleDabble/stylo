# Too get tweepy to import use:
# conda install -c conda-forge tweepy

# Then in anaconda package manager, make sure it includes the conda-forge channel
import tweepy
import io
import json
import re


# Initialize Settings For Tweepy loading Config file
with open('../config/config.json', 'r') as f:
    config = json.load(f)
config = config['twitter']

auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
auth.set_access_token(config['access_token'], config['access_token_secret'])
api = tweepy.API(auth)

def remove_url(comment):
    return re.sub('(https?://)?(([a-zA-Z0-9]+)\.)+[a-zA-Z]{2,}(/[a-zA-Z0-9;/+\-%@,!^*&?:}{_=\\\]+)?(\.[a-zA-Z]+)?',
                  'url', comment)

class twitScrape():
    def getIndivTweets(self, username):
        path = '../corpora/twitter_corpus/'
        save_path = path + username + ".txt"
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
                w.write(user_tweets[:240*50])
            return 1
        except:
            print('Failed to find user')
            return -1
                    
