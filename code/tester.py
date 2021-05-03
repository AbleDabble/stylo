from IdentModel import start_identification_reddit, start_identification_twitter
from verifModel import start_verification_reddit, start_verification_twitter
import argparse
import os



def main():
    parser = argparse.ArgumentParser(description='Perform tests')
    parser.add_argument('platform', choices=['r','t'], help='Choose [r]eddit or [t]witter')
    parser.add_argument('-m', '--model', dest='model', choices=['id','vf','a'], help='Which model to test',default='a')
    parser.add_argument('-u','--user', dest='user', nargs='+', help='Change default users')
    args = parser.parse_args()
    twitter_default = ['CNN', 'jimcramer']
    reddit_default = ['Baerog', '4Darco']
    if args.platform == 'r':
        if len(args.user) == 0:
            users = reddit_default
        

    if len(args.user) == 0:
        

    
if __name__ == '__main__':
    main()
