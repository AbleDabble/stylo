import praw
import prawcore.exceptions


class redditScraper():

    # Start reddit Instance
    def redditInst(self):
        try:
            reddit = praw.Reddit(client_id="IKj8CIYn9x5MGA",
                                 client_secret="LnkdvmTfJiS0iJFKLc3q1CuWtRo0aQ",
                                 password="Hopihop1",
                                 user_agent="Auth_Id",
                                 username="what_database")
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
        if reddit_user == -1:
            return -1
        try:
            reddit_user.redditor(username)
        except prawcore.exceptions.NotFound as e:
            print(e)

        user_comment = []
        user = reddit_user.redditor(username)

        while len(user_comment) <= 100:
            try:
                for comment in user.comments.new(limit=None):
                    cur_comment = comment.body
                    if len(cur_comment) > 350 and self.is_english(cur_comment):
                        user_comment.append(cur_comment)
            except prawcore.exceptions.NotFound as e:
                print("\nCould not find user", username)
                print(e)
                break
            except prawcore.exceptions.OAuthException as e:
                print("\nAuthentication Error: Check reddit account credentials\n", e)
                break

        if len(user_comment) == 0:
            return 0
        else:
            path = self.writeComments(user_comment, username)
            if path == -1:
                return 0
            else:
                return path