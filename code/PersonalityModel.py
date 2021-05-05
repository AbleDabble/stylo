from Personality import Personality
from reddit_Scrape import redditScraper
from Twitterscrape import twitScrape
import os

reddit_corpus = '../corpora/reddit_corpus/'
twitter_corpus = '../corpora/twitter_corpus/'

def print_progress(stage, message, num_stages=4):
    out = '[' + '=' * stage + ' ' * (num_stages - stage) + '] ' + message
    print(' ' * 80, end='\r')
    if stage != num_stages: print(out, end='\r')
    else: print(out)



def start_personality(username, downloader, root_corpus):
    curr_downloads = set([f[:-4] for f in os.listdir(root_corpus) if f.endswith('.txt')])
    def download_user(user):
        if user not in curr_downloads:
            print_progress(0, f'Downloading User {user}')
            r = downloader(user)
            if type(r) == int and r < 1:
                print(f'Download for user {user} failed')
                return r
            return 1
        else: return 1

    if download_user(username) < 1: return -1

    # Create file path
    user_path = root_corpus + username + '.txt'
    with open(user_path, 'r') as f:
        comments = user_path
    model = Personality()
    results = model.predict(comments)
    print('Results = ', results)
    return results

def start_personality_reddit(user):
    def downloader(user):
        rs = redditScraper()
        return rs.getUserComments(user)
    return start_personality(user, downloader, reddit_corpus)

def start_personality_twitter(user):
    def downloader(user):
        tw = twitScrape()
        return tw.getIndivTweets(user)
    return start_personality(user, downloader, twitter_corpus)

if __name__ == '__main__':
    start_personality_reddit('Baerog')

    

    


