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


def start_identification_reddit(user_list, text):
    rs = redditScraper()
    current_users = [user[:-4] for user in os.listdir('../corpora/reddit_corpus') if user.endswith('.txt')][:50]
    user_paths = []
    current_users_length = 0
    user_label_names = {}
    for user in user_list:
        if user not in current_users:
            ret = rs.getUserComments(user)
            if ret == 0:
                print(f'Problem downloading comments for user {user}')
        user_paths.append(ret) 
    user_profiles = []
    current_users = ['../corpora/reddit_corpus/' + user + '.txt' for user in current_users]
    current_users += user_list
    for i, path in enumerate(current_users):
        user_profiles.append(IdentProfile(path, current_class=current_users_length).create_profile())
        user_label_names[i] = path
    text_df = IdentText('', text)
    svc = SVC(kernel='poly')
    df = pd.concat(user_profiles).reset_index()
    target = df['target']
    df = df.drop('target', axis=0)
    pipe = Pipeline([("MinMaxScaler", MinMaxScaler()), ('ED', ED()), ('MIFS', MIFS()), ('SVC', SVC(kernel='poly', class_weight={0:1, 1:100}, degree=3))])
    pipe.fit(df, target)
    prediction = pipe.predict(text_df)
    print(user_label_names[prediction])
    return user_label_names[prediction]




        
start_identification_reddit(['Baerog'],"This is a text block. This should be about 350 characters and probably will not be that large. Therefor it will be probably be smaller or maybe even bigger I don't know. It is hard to tell if this is 350 characters. More words and more text and more and more and more. This is the way things are go go. Power puff girls.")
