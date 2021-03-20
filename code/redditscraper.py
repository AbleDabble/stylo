import os
from psaw import PushshiftAPI
import io
import re

def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

def remove_url(comment):
    return re.sub('(https?://)?(([a-zA-Z0-9]+)\.)+[a-zA-Z]{2,}(/[a-zA-Z0-9;/+\-%@,!^*&?:}{_=\\\]+)?(\.[a-zA-Z]+)?', 'url', comment)
    
    
def correct_comments(author, size, api):
    gen = api.search_comments(limit=100, filter=["author", "body", "created_utc"], author=author)
    comments = list(gen)
    comment_bodies = [remove_url(comment.body) for comment in comments if len(remove_url(comment.body)) >= size]
    length = len(comments)
    while length == 100:
        current_comment = comments[len(comments)-1]
        gen = api.search_comments(limit=100, filter=["author", "body", "created_utc"], author=author, before=current_comment.created_utc)
        #if current_comment.author != author:
        #   raise ValueError("The Current author is not what it should be")
        tmp = list(gen)
        if tmp[1].created_utc >= current_comment.created_utc:
            raise ValueError("Not Retrieving previous commnents")
        length = len(tmp)
        comments += tmp
        comment_bodies += [remove_url(comment.body) for comment in tmp if len(remove_url(comment.body)) >= size]
        if len(comment_bodies) >= 60:
            break
    return comment_bodies

def download(author, size):
    path = '../corpora/reddit_corpus/'
    end_of_com_indic = "\n!#$%@&"
    #print("authors length", len(authors))
    api = PushshiftAPI()
    size = 350
    save_path = path + author + ".txt"
    comments = correct_comments(author, size, api)
    if len(comments) == 0:
      raise ValueError("No Comments found for user")
    print(len(comments), "comments for", author)
    save = ""
    count = 0
    for comment in comments:
        save += comment[:size]
        count += 1
        if count >= 60:
            break
    with io.open(save_path, "w", encoding="utf-8") as w:
        w.write(save)
    return save_path