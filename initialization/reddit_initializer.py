import sys
sys.path.append('../code/')
from IdentProfile import IdentProfile
import os
import json

path = '../corpora/reddit_corpus/'

labels = {'new_label':0,'labels':{}}
user_paths = [path + user for user in os.listdir(path) if user.endswith('.txt')]
user_names = [user[:-4] for user in os.listdir(path) if user.endswith('.txt')]

for path, name in zip(user_paths, user_names):
    print(f'User {name} started label: {labels["new_label"]}')
    ip = IdentProfile(path, labels['new_label'])
    labels['labels'][labels['new_label']] = name
    labels['new_label'] += 1
    df = ip.create_profile()
    df.to_csv(f'../corpora/reddit_corpus_csv/{name}.csv',index=False)

with open('../config/labels.json', 'w') as f:
    json.dump(labels, f)
