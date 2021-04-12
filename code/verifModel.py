from Profile import Profile
from sklearn.svm import LinearSVC, SVC
from EntropyDiscretization import EntropyDiscretization as ED
from MIFS import MIFS
from imblearn.over_sampling import RandomOverSampler
from imblearn.pipeline import Pipeline
from MIFS import MIFS
from redditscraper import correct_comments
from redditscraper import download
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import os

reddit_path = "../corpora/reddit_corpus/"

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
  curr_downloads = set([f[:-4] for f in os.listdir('../corpora/reddit_corpus/') if f.endswith('.txt')])
  if user2 not in curr_downloads:
    profile2 = Profile(download(user2, 350))
  else:
    profile2 = Profile(reddit_path + user2 + ".txt")
  if user1 not in curr_downloads:
    profile1 = Profile(download(user1, 350), reddit_path + user2 + ".txt")
  else:
    profile1 = Profile(reddit_path + user1 + ".txt", reddit_path + user2 + ".txt")
  
  print("Creating Profile for user: ", user1)
  df_user1 = profile1.create_profile()
  print("Creating Profile for user: ", user2)
  df_user2 = profile2.extract_positives()
  print("Done")
  x, y = split_x_y(df_user1, numpy=True)
  pipe = Pipeline([("MinMaxScaler", MinMaxScaler()), ('ED', ED()), ('MIFS', MIFS()), ('SVC', SVC(kernel='poly', class_weight={0:1, 1:100}, degree=1))])
  print("Beginning Training")
  pipe.fit(x, y)
  user2_x, user2_y = split_x_y(df_user2, numpy=True)
  count = 0
  print("Making up results")
  #for sample in user2_x:
  predictions = pipe.predict(user2_x)
  print(len(predictions))
  count = np.sum(predictions)
  print("The chances these two users are the same is: ", count / len(user2_x))
  liklihood = count / len(user2_x)
  if liklihood < 0.6:
    return False
  return True 


  # return count / len(user2_x)

start_verification_reddit("Baerog", "Baerog")