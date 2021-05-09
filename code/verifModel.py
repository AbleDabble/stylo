from Profile import Profile
from sklearn.svm import LinearSVC, SVC
from EntropyDiscretization import EntropyDiscretization as ED
from MIFS import MIFS
from MIFS import MIFS
#from sklearn.pipeline import Pipeline
from imblearn.pipeline import Pipeline
from reddit_Scrape import redditScraper
from sklearn.preprocessing import MinMaxScaler
from Twitterscrape import twitScrape
from VerifProfile import VerifProfile
import numpy as np
import os

reddit_path = "../corpora/reddit_corpus/"
twitter_path = '../corpora/twitter_corpus/'

def split_x_y(df, numpy=False):
    y = df["target"].copy()
    x = df.drop("target", axis=1)
    if numpy:
        x = x.to_numpy()
        y = y.to_numpy()
    return x, y

def print_progress(stage, message, num_stages=4):
    out = '[' + '=' * stage + ' ' * (num_stages - stage) + '] ' + message
    print(' ' * 80, end='\r')
    if stage != num_stages: print(out, end='\r')
    else: print(out)

def start_verification(user1, user2, downloader, root_corpus, comment_size):
    '''This method starts the user verification model, trains it and comapres the two users to
    determine if they are the same.

    Returns: True if users are the same
    Returns: False if the user are not the same
    '''
    print_progress(0, '')
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

    if download_user(user1) < 1: return -1
    if download_user(user2) < 1: return -1

    user1_path = root_corpus + user1 + ".txt"
    user2_path = root_corpus + user2 + ".txt"

    print_progress(1, f'Generating Profiles for users {user1} and {user2}')

    verifier = VerifProfile(user1_path, user2_path, email_size=comment_size)
    train_df, test_df = verifier.create_profile()
    x_train, y_train = split_x_y(train_df, numpy=True)
    
    # Create the pipeline for the data
    pipe = Pipeline([
        ("MinMaxScaler", MinMaxScaler()),
        ('ED', ED()),
        ('MIFS', MIFS()),
        ('SVC', SVC(kernel='poly', class_weight={0:0.0125, 1: 1}, degree=3))
        ]) #type: ignore
    # Train the data
    print_progress(2, 'Training Model')
    pipe.fit(x_train, y_train)
    x_test = test_df.to_numpy()

    print_progress(3, 'Comparing Users')

    predictions = pipe.predict(x_test)
    count = np.count_nonzero(predictions)

    likelihood = count/len(predictions)
    print_progress(4, f'Proportion of comments that match: {likelihood}')

    if likelihood < 0.65:
        return False
    else:
        return True

def start_verification_reddit(user1, user2):
    def downloader(user):
        rs = redditScraper()
        return rs.getUserComments(user)
    return start_verification(user1, user2, downloader, reddit_path, 350)

def start_verification_twitter(user1, user2):
    def downloader(user):
        tw = twitScrape()
        return tw.getIndivTweets(user)
    return start_verification(user1, user2, downloader, twitter_path, 240)


