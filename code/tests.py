from verifModel import start_verification_reddit, start_verification_twitter
from IdentModel import start_identification_twitter, start_identification_reddit
import os

print('TWITTER VERIFICATION')
start_verification_twitter('CNN', 'jimcramer')

print('DOWNLOADING TEST')
print('\tAttempting to download Michael Malice')

os.remove('../corpora/twitter_corpus/michaelmalice.txt')
start_verification_twitter('CNN', 'michaelmalice')
try:
    print('File size:', os.path.getsize('../corpora/twitter_corpus/michaelmalice.txt'))
except OSError:
    print('ERROR: File Does not exist or could not be found')

print('REDDIT VERIFICATION')
start_verification_reddit('Baerog', 'chafedogg')

print('DOWNLOADING TEST')
print('\tAttempting to download luncheroo')
os.remove('../corpora/reddit_corpus/luncheroo.txt')
start_verification_reddit('Baerog', 'luncheroo')

try:
    print('File size:', os.path.getsize('../corpora/reddit_corpus/luncheroo.txt'))
except OSError:
    print('ERROR: file does not exist or could not be found')

print('IDENTIFICATION TWITTER')

text = 'I am staring down the empty abyss of life and have lost all meaning. Penniless and at the end of my supply of the drug which alone gives life meaning, I will casy myself from this garret window to the squalid street below'

start_identification_twitter(['CNN', 'Adele', 'garyvee', 'jimcramer'], text)

print('REDDIT IDENTIFICATION')


text = 'I am staring down the empty abyss of life and have lost all meaning. Penniless and at the end of my supply of the drug which alone gives life meaning, I will casy myself from this garret window to the squalid street below. Do not judge me for my addiction to morphine. It is my hope that after these hastily scrawled pages that you understand'

start_identification_reddit(['Baerog', '4Darco','artchang','externality'], text)

