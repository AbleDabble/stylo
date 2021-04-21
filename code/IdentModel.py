import numpy as np
import pandas as pd
from IdentProfile import IdentProfile, IdentText
from reddit_Scrape import redditScraper
import os
from sklearn.svm import SVC
from EntropyDiscretization import EntropyDiscretization as ED
from MIFS import MIFS
from imblearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
import json

PATH = '../corpora/reddit_corpus_csv/'

def split_x_y(df, numpy=False):
    y = df["target"].copy()
    x = df.drop("target", axis=1)
    if numpy:
        x = x.to_numpy()
        y = y.to_numpy()
    return x, y


def start_identification_reddit(user_list, text):
    rs = redditScraper()
    user_profiles = []
    with open('../config/labels.json', 'r') as f:
        labels = json.load(f)
    
    # Create a list of already downloaded users
    downloaded_users = [user[:-4] for user in os.listdir(PATH) if user.endswith('.csv')]

    # Read and add users from already downloaded
    #for user in downloaded_users[:10]:
    #    path = PATH + user + '.csv'
    #    user_profiles.append(pd.read_csv(path))
        
    # check if downloaded and if not download
    for user in user_list:
        if user in downloaded_users or len(user) == 0:
            continue
        try:
            path = rs.getUserComments(user)
            ip = IdentProfile(path, labels['new_label'])
            labels['labels'][labels['new_label']]= user
            labels['new_label'] += 1
            df = ip.create_profile()
            df.to_csv(f'../corpora/reddit_corpus_csv/{user}.csv', index=False)
            user_profiles.append(df.copy())
            print('created new user profile', user)
        except:
            print(f'Failed to download user: {user}')   
    with open('../config/labels.json', 'w') as f:
        json.dump(labels, f)

    # Train the model on the users
    df = pd.concat(user_profiles, ignore_index=True)
    x, y = split_x_y(df, numpy=True)
    pipe = Pipeline([
        ("MinMaxScaler", MinMaxScaler()),
        ('ED', ED()),
        ('MIFS', MIFS()),
        ('SVC', SVC(kernel='poly', degree=3))]) # type: ignore
    print('beginning training')
    pipe.fit(x, y)

    # Create a dataframe of the text
    ip = IdentText('', text)
    text_df = ip.create_profile()
    x_test  = text_df.to_numpy()
    prediction = pipe.predict(x_test)
    prediction = prediction[0]
    # determine which label corresponds to the prediction
    choice = labels['labels'][str(prediction)]
    print('Best candidate', choice)
    return choice



#start_identification_reddit(['Baerog'],"This is a text block. This should be about 350 characters and probably will not be that large. Therefor it will be probably be smaller or maybe even bigger I don't know. It is hard to tell if this is 350 characters. More words and more text and more and more and more. This is the way things are go go. Power puff girls. There is more letters to add. Now we will continue to add more letters. This will have more letters and characters. There need to be a lot of fucking characters. How about that. There is this thing and it works so well. IT works GREAT. IT WORKS AMAZING.")
