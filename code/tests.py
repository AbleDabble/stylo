from verifModel import start_verification_reddit, start_verification_twitter
from IdentModel import start_identification_twitter, start_identification_reddit
import os
import json

twitter_config_path = '../config/labels_twitter.json'
reddit_config_path = '../config/labels.json'
with open(twitter_config_path, 'r') as f:
    twitter_config = json.load(f) 

with open(reddit_config_path, 'r') as f:
    reddit_config = json.load(f)



print('IDENTIFICATION TWITTER')

text = 'I am staring down the empty abyss of life and have lost all meaning. Penniless and at the end of my supply of the drug which alone gives life meaning, I will casy myself from this garret window to the squalid street below. More words and characters. I think this is more than enoguh by to be sure I am going to continue to write more characters. Until I have a lot of characters. '

start_identification_twitter(['CNN', 'Adele', 'garyvee', 'jimcramer'], text)

print('REDDIT IDENTIFICATION')


text = 'I am staring down the empty abyss of life and have lost all meaning. Penniless and at the end of my supply of the drug which alone gives life meaning, I will casy myself from this garret window to the squalid street below. Do not judge me for my addiction to morphine. It is my hope that after these hastily scrawled pages that you understand. Need more characters holy shit. '

start_identification_reddit(['Baerog', '4Darco','artchang','externality'], text)




print('TWITTER VERIFICATION')
start_verification_twitter('CNN', 'jimcramer')

print('DOWNLOADING TEST')
print('\tAttempting to download Michael Malice')

start_verification_twitter('CNN', 'michaelmalice')

try:
    print('File size:', os.path.getsize('../corpora/twitter_corpus/michaelmalice.txt'))
    os.remove('../corpora/twitter_corpus/michaelmalice.txt')
except OSError:
    print('ERROR: File Does not exist or could not be found')

with open(twitter_config_path, 'w') as f:
    json.dump(twitter_config, f)

print('REDDIT VERIFICATION')
start_verification_reddit('Baerog', 'chafedogg')

print('DOWNLOADING TEST')
print('\tAttempting to download luncheroo')
start_verification_reddit('Baerog', 'luncheroo')

try:
    print('File size:', os.path.getsize('../corpora/reddit_corpus/luncheroo.txt'))
    os.remove('../corpora/reddit_corpus/luncheroo.txt')
except OSError:
    print('ERROR: file does not exist or could not be found')

with open(reddit_config_path, 'w') as f:
    json.dump(reddit_config, f)


