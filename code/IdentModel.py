import numpy as np
import pandas as pd
from IdentProfile import IdentProfile, IdentText
from reddit_Scrape import redditScraper
import os
from sklearn.svm import LinearSVC
from EntropyDiscretization import EntropyDiscretization as ED
from MIFS import MIFS
from imblearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from Twitterscrape import twitScrape
import json

REDDIT_PATH = '../corpora/reddit_corpus_csv/'
TWITTER_PATH = '../corpora/twitter_corpus_csv/'

def split_x_y(df, numpy=False):
    y = df["target"].copy()
    x = df.drop("target", axis=1)
    if numpy:
        x = x.to_numpy()
        y = y.to_numpy()
    return x, y


def start_identification_reddit(user_list, text):
    if len(text) < 350:
        print('Text Length must be 350 characters. Currently:', len(text))
    rs = redditScraper()
    user_profiles = []
    with open('../config/labels.json', 'r') as f:
        labels = json.load(f)
    
    # Create a list of already downloaded users
    downloaded_users = [user[:-4] for user in os.listdir(REDDIT_PATH) if user.endswith('.csv')]
    #print('Downloaded_users', downloaded_users)
    # Read and add users from already downloaded
    #for user in downloaded_users[:10]:
    #    path = PATH + user + '.csv'
    #    user_profiles.append(pd.read_csv(path))
        
    # check if downloaded and if not download
    user_list = [user for user in user_list if len(user) > 0]
    for user in user_list:
        if user in downloaded_users or len(user) == 0:
            user_profiles.append(pd.read_csv(f'../corpora/reddit_corpus_csv/{user}.csv'))
            continue
        try:
            path = rs.getUserComments(user)
            if type(path) == int:
                print('problem downloading user', user)
                continue
            ip = IdentProfile(path, labels['new_label'])
            labels['labels'][labels['new_label']]= user
            labels['new_label'] += 1
            df = ip.create_profile()
            df.to_csv(f'../corpora/reddit_corpus_csv/{user}.csv', index=False)
            user_profiles.append(df.copy())
            print('created new user profile for ', user)
        except:
            print(f'Failed to download user: {user}')   
    with open('../config/labels.json', 'w') as f:
        json.dump(labels, f)

    # Train the model on the users
    df = pd.concat(user_profiles, ignore_index=True)
    x, y = split_x_y(df, numpy=True)
    pipe = Pipeline([
        ("MinMaxScaler", MinMaxScaler()),
        #('ED', ED()),
        #('MIFS', MIFS(low=0)),
        ('SVC', LinearSVC(C=0.5, penalty='l2',dual=True))]) # type: ignore
    print('beginning training')
    pipe.fit(x, y)

    # Create a dataframe of the text
    ip = IdentText('', text)
    text_df = ip.create_profile()
    x_test  = text_df.to_numpy()
    prediction = pipe.predict(x_test)
    prediction = prediction[0]
    print('prediction = ', prediction)
    # determine which label corresponds to the prediction
    choice = labels['labels'][str(prediction)]
    print('Best candidate', choice)
    return choice

def start_identification_twitter(user_list, text):
    if len(text) < 240:
        print('Text Length must be 240 characters. Currently:', len(text))
        return -1
    tw = twitScrape()
    user_profiles = []
    with open('../config/labels_twitter.json', 'r') as f:
        labels = json.load(f)
    downloaded_users = [user[:-4] for user in os.listdir(TWITTER_PATH) if user.endswith('.csv')]
    user_list = [user for user in user_list if len(user) > 0]
    for user in user_list:
        if user in downloaded_users:
            user_profiles.append(pd.read_csv(f'{TWITTER_PATH}{user}.csv'))
            continue
        r = tw.getIndivTweets(user)
        if r <= -1:
            continue

        user_path = TWITTER_PATH + user + '.txt'
        ip = IdentProfile(user_path, labels['new_label'], email_size=240)
        labels['labels'][labels['new_label']] = user
        labels['new_label'] += 1
        df = ip.create_profile()
        df.to_csv(f'../corpora/twitter_corpus_csv/{user}.csv', index=False)
        user_profiles.append(df.copy())
        print('created new user profile for ', user)
    with open('../config/labels_twitter.json', 'w') as f:
        json.dump(labels, f)
    df = pd.concat(user_profiles, ignore_index=True)
    x, y = split_x_y(df, numpy=True)
    pipe = Pipeline([
            ('MinMaxScaler', MinMaxScaler()),
            ('SVC', LinearSVC(C=0.5, penalty='l2', dual=True))
            ]) # type: ignore
    print('Beginning Training')
    pipe.fit(x, y)
    ip = IdentText('', text, email_size=240)
    text_df = ip.create_profile()
    x_test = text_df.to_numpy()
    prediction = pipe.predict(x_test)
    prediction = prediction[0]
    print('prediction', prediction)
    choice = labels['labels'][str(prediction)]
    print('Best candidate', choice)
    return choice


        



#start_identification_reddit(['Baerog', '4Darco', 'ScrotumTotums', 'OrionLax'],"This is a text block. This should be about 350 characters and probably will not be that large. Therefor it will be probably be smaller or maybe even bigger I don't know. It is hard to tell if this is 350 characters. More words and more text and more and more and more. This is the way things are go go. Power puff girls. There is more letters to add. Now we will continue to add more letters. This will have more letters and characters. There need to be a lot of fucking characters. How about that. There is this thing and it works so well. IT works GREAT. IT WORKS AMAZING.")
