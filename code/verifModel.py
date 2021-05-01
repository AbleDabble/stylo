from Profile import Profile
from sklearn.svm import LinearSVC, SVC
from EntropyDiscretization import EntropyDiscretization as ED
from MIFS import MIFS
from imblearn.over_sampling import RandomOverSampler
from imblearn.pipeline import Pipeline
from MIFS import MIFS
from sklearn.pipeline import Pipeline
from reddit_Scrape import redditScraper
from sklearn.preprocessing import MinMaxScaler
from Twitterscrape import twitScrape
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


def start_verification_reddit(user1, user2):
    '''This method starts the user verification model, trains it and comapres the two users to
    determine if they are the same.

    Returns: True if users are the same
    Returns: False if the user are not the same
    '''
    red_scraper = redditScraper()
    '''If the users comment file cannot be genterated then return False
     TO-DO: find a better solution/return value for this'''

    curr_downloads = set([f[:-4] for f in os.listdir('../corpora/reddit_corpus/') if f.endswith('.txt')])
    if user1 not in curr_downloads:
        user1_comments = red_scraper.getUserComments(user1)
        print('user1_comments type:', type(user1_comments))
        if type(user1_comments) == int:
            if user1_comments <= 0:
                return user1_comments
        profile2 = Profile(user1_comments)
    else:
        profile2 = Profile(reddit_path + user1 + ".txt")
    if user2 not in curr_downloads:
        user2_comments = red_scraper.getUserComments(user2)
        print('user2_comments type:', type(user2_comments))
        if type(user2_comments) == int:
            if user2_comments <= 0:
                return user2_comments
        profile1 = Profile(user2_comments, reddit_path + user2 + ".txt")
    else:
        profile1 = Profile(reddit_path + user2 + ".txt", reddit_path + user1 + ".txt")

    print("Creating Profile for user: ", user1)
    df_user1 = profile1.create_profile()
    print("Creating Profile for user: ", user2)
    df_user2 = profile2.extract_positives()
    print("Done")
    x, y = split_x_y(df_user1, numpy=True)
    pipe = Pipeline([("MinMaxScaler", MinMaxScaler()), ('ED', ED()), ('MIFS', MIFS()),
                     ('SVC', SVC(kernel='poly', class_weight={0: 1, 1: 40}, degree=3))])
    print("Beginning Training")
    pipe.fit(x, y)
    user2_x, user2_y = split_x_y(df_user2, numpy=True)
    count = 0
    # for sample in user2_x:
    predictions = pipe.predict(user2_x)
    print(len(predictions))
    count = np.sum(predictions)
    print("The chances these two users are the same is: ", count / len(user2_x))
    liklihood = count / len(user2_x)
    if liklihood < 0.85:
        return False
    return True


def start_verification_twitter(user1, user2):
    '''This method starts the user verification model, trains it and comapres the two users to
    determine if they are the same.

    Returns: True if users are the same
    Returns: False if the user are not the same
    '''
    tw = twitScrape()
    '''If the users comment file cannot be genterated then return False
     TO-DO: find a better solution/return value for this'''

    curr_downloads = set([f[:-4] for f in os.listdir('../corpora/twitter_corpus/') if f.endswith('.txt')])
    if user2 not in curr_downloads:
        user1_comments = twitScrape.getIndivTweets(user1)
        if user1_comments == 0:
            Exception(f'Problem downloading user {user1}')
    profile2 = Profile(twitter_path + user1 + ".txt",email_size=240)
    if user1 not in curr_downloads:
        user2_comments = twitScrape.getIndivTweets(user2)
        if user2_comments == 0:
            Exception(f'Problem downloading user {user2}')
    profile1 = Profile(twitter_path + user2 + ".txt", twitter_path + user1 + ".txt", email_size=240)

    print("Creating Profile for user: ", user1)
    df_user1 = profile1.create_profile()
    print("Creating Profile for user: ", user2)
    df_user2 = profile2.extract_positives()
    print("Done")
    x, y = split_x_y(df_user1, numpy=True)
    pipe = Pipeline([("MinMaxScaler", MinMaxScaler()), ('ED', ED()), ('MIFS', MIFS()),
                     ('SVC', SVC(kernel='poly', class_weight={0: 1, 1: 40}, degree=3))])
    print("Beginning Training")
    pipe.fit(x, y)
    user2_x, user2_y = split_x_y(df_user2, numpy=True)
    count = 0
    # for sample in user2_x:
    predictions = pipe.predict(user2_x)
    print(len(predictions))
    count = np.sum(predictions)
    print("The chances these two users are the same is: ", count / len(user2_x))
    liklihood = count / len(user2_x)
    if liklihood < 0.85:
        return False
    return True


def start_verification_twitter(user1, user2):
    '''This method starts the user verification model, trains it and comapres the two users to
    determine if they are the same.

    Returns: True if users are the same
    Returns: False if the user are not the same
    '''
    tw = twitScrape()
    '''If the users comment file cannot be genterated then return False
     TO-DO: find a better solution/return value for this'''

    curr_downloads = set([f[:-4] for f in os.listdir('../corpora/twitter_corpus/') if f.endswith('.txt')])
    if user2 not in curr_downloads:
        user1_comments = twitScrape.getIndivTweets(user1)
        if user1_comments == -1:
            Exception(f'Problem downloading user {user1}')
        profile2 = Profile(user1_comments, email_size=240)
    else:
        profile2 = Profile(reddit_path + user2 + ".txt")
    if user1 not in curr_downloads:
        user2_comments = twitScrape.getIndivTweets(user2)
        if user2_comments == -1:
            Exception(f'Problem downloading user {user2}')
        profile1 = Profile(user2_comments, reddit_path + user2 + ".txt",email_size=240)
    else:
        profile1 = Profile(reddit_path + user1 + ".txt", reddit_path + user2 + ".txt", email_size=240)

    print("Creating Profile for user: ", user1)
    df_user1 = profile1.create_profile()
    print("Creating Profile for user: ", user2)
    df_user2 = profile2.extract_positives()
    print("Done")
    x, y = split_x_y(df_user1, numpy=True)
    pipe = Pipeline([("MinMaxScaler", MinMaxScaler()), ('ED', ED()), ('MIFS', MIFS()),
                     ('SVC', SVC(kernel='poly', class_weight={0: 1, 1: 40}, degree=3))])
    print("Beginning Training")
    pipe.fit(x, y)
    user2_x, user2_y = split_x_y(df_user2, numpy=True)
    count = 0
    print("Making up results")
    # for sample in user2_x:
    predictions = pipe.predict(user2_x)
    print(len(predictions))
    count = np.sum(predictions)
    print("The chances these two users are the same is: ", count / len(user2_x))
    liklihood = count / len(user2_x)
    if liklihood < 0.85:
        return False
    return True

