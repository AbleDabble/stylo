import numpy as np
import pandas as pd
from IdentProfile import IdentProfile, IdentText
from .reddit_Scrape import redditScraper
import os
from sklearn.svm import SVC
from EntropyDiscretization import EntropyDiscretization as ED
from MIFS import MIFS
from imblearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler

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

    downloaded_users = {user[:-4] for user in os.listdir('../corpora/reddit_corpus/') if user.endswith('.txt')}
    # Download new users or if already downloaded add them 
    # their profile to the list
    for user in user_list: 
      if user in downloaded_users:
        continue
      path = rs.getUserComments(user)
      ip = IdentProfile(path)
      
    




    x, y = split_x_y(df, numpy=True)
    print('y',y)
    pipe = Pipeline([
        ("MinMaxScaler", MinMaxScaler()),
        ('ED', ED()),
        ('MIFS', MIFS()),
        ('SVC', SVC(kernel='poly', degree=3))]) # type: ignore
    pipe.fit(x, y)
    x_test = text_df.to_numpy()
    prediction = pipe.predict(x_test)
    print(user_label_names[prediction])
    return user_label_names[prediction]



start_identification_reddit(['Baerog'],"This is a text block. This should be about 350 characters and probably will not be that large. Therefor it will be probably be smaller or maybe even bigger I don't know. It is hard to tell if this is 350 characters. More words and more text and more and more and more. This is the way things are go go. Power puff girls. There is more letters to add. Now we will continue to add more letters. This will have more letters and characters. There need to be a lot of fucking characters")
