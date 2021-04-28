import re
import praw
import prawcore.exceptions
import json


class redditScraper():

    # Start reddit Instance
    def redditInst(self):
        try:
            with open('../config/config.json', 'r') as f:
                config = json.load(f)
            config = config['reddit']
            reddit = praw.Reddit(client_id=config['client_id'],
                                 client_secret=config['client_secret'],
                                 password=config['password'],
                                 user_agent=config['user_agent'],
                                 username=config['username'])
        except prawcore.OAuthException as e:
            return -1
        return reddit

    # Checks for english comments
    def is_english(self, comment_string):
        try:
            comment_string.encode(encoding='utf-8').decode('ascii')
        except UnicodeError:
            return False
        else:
            return True

    def remove_url(self, comment):
        return re.sub('(https?://)?(([a-zA-Z0-9]+)\.)+[a-zA-Z]{2,}(/[a-zA-Z0-9;/+\-%@,!^*&?:}{_=\\\]+)?(\.[a-zA-Z]+)?',
                      'url', comment)

    # Writes an array of comments to a file and saves a txt file
    # to the reddit corpus with the username as the title.
    # Returns a 1 if successful, 0 if any errors occurred
    def writeComments(self, commentList, filename):
        path = '../corpora/reddit_corpus/'
        comp_name = path + filename + ".txt"
        try:
            file = open(comp_name, "w")
        except FileNotFoundError as e:
            print("Could not open: ", filename)
            print(e)
            return -1
        file.writelines(commentList)
        file.close()
        return comp_name

    def getUserComments(self, username):
        reddit_user = self.redditInst()
        size = 1
        if reddit_user == -1:
            return -1
        try:
            reddit_user.redditor(username)
        except prawcore.exceptions.NotFound as e:
            print(e)

        user_comment = []
        user = reddit_user.redditor(username)

        while size < 17500:
            try:
                for comment in user.comments.new(limit=None):
                    cur_comment = comment.body
                    cur_comment = self.remove_url(cur_comment)
                    if size <= 17500:
                        if len(cur_comment) > 350 and self.is_english(cur_comment):
                            #print("Should be a vaild comment", len(cur_comment))
                            size = size + len(cur_comment)
                            print("Current Size of comment array", size)
                            user_comment.append(cur_comment)
                    else:
                        print(size)
                        print(len(user_comment))
                        break
            except prawcore.exceptions.NotFound as e:
                print("\nCould not find user", username)
                print(e)
                return -1
            except prawcore.exceptions.OAuthException as e:
                print("\nAuthentication Error: Check reddit account credentials\n", e)
                return -1
            if len(user_comment) == 0:
                break

        if len(user_comment) == 0:
            print("No comments found for user")
            return 0
        else:
            path = self.writeComments(user_comment, username)
            if path == -1:
                return 0
            else:
                print(user_comment)
                print(len(user_comment))
                print(size)
                return path