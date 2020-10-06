import re
from email.parser import Parser
import os

def email_body(path):
    with open(path, "r") as r:
        data = r.read()
    email = Parser().parsestr(data)
    body = email.get_payload().split("-----")[0]
    if len(body) < 500:
        return ''
    body = re.sub('[0-9]+%', 'XX%', body)
    body = re.sub('\$[0-9.]+', '$XX', body)
    body = re.sub('[a-zA-Z0-9.\-]+@[a-zA-Z0-9.\-]+', 'email', body)
    body = re.sub('http://[A-Za-z0-9.\-/]*', 'http', body)
    body = re.split('.*\n.*\nTo:', body)[0]
    body = re.split('To:', body)[0]
    body = re.split('From: .*\nTo:[\.\n]*', body)[0]
    body = re.split('From: ', body)[0]
    body = re.split('ClickAtHomePilot', body)[0]
    boyd = re.split('.*\nSent by:', body)[0]
    body = remove_time(body)
    body = remove_phone(body)
    body = re.sub('=\n', '', body)
    body = re.sub('[0-9]+.[0-9]+|[0-9]+', 'numb', body)
    body = re.sub(' +', ' ', body) # Normalize spacing
    body = re.sub('(\n\n)+', '\n\n', body) # Normalize new lines characters
    return body

def remove_time(body):
    """Removes time and date: replace time with meta-tag time
    replaces date with meta-tag date"""
    time = re.compile('([0-9]+):([0-9]+) *PM|([0-9]+):([0-9]+) *AM', re.I)
    date = re.compile('[0-9]+/[0-9]+/[0-9]+')
    body = re.sub(time, 'time', body)
    body = re.sub(date, 'date', body)
    return body

def remove_phone(body):
    """Removes phone numbers and replaces it with phone"""
    phone = re.compile('[0-9]{7}|[0-9]{3}[\- ][0-9]{3}[\- ][0-9]{4}|[0-9]{10}|\([0-9]{3}\)[\- ][0-9]{3}[\- ][0-9]{4}')
    body = re.sub(phone, 'phone', body)
    return body
    


def get_email_bodies(email_root, out_root):
    """Returns a the emails that are greater than 500 characters in length
        for people with 50 instances
        looks in sent_items and sent"""
    all_acc = [os.path.join(email_root, f) for f in os.listdir(email_root)]
    for acc in all_acc:
        sent = os.path.join(acc, 'sent')
        count = 0
        sent_items = os.path.join(acc, 'sent_items')
        if os.path.isdir(sent):
            emails = [os.path.join(sent, f) for f in os.listdir(sent) if not f.endswith('.ipynb_checkpoints')]
            emails = [f for f in emails if not f.endswith('clickathome')]
            outdir = os.path.join(out_root, os.path.split(acc)[1])
            os.makedirs(outdir, exist_ok=True)
            for email in emails:
                body = email_body(email)
                if len(body) > 500 and len(body) < 30000:
                    with open(os.path.join(outdir, str(count)), "w") as w:
                        w.write(body)
                        count += 1
        if os.path.isdir(sent_items):
            emails = [os.path.join(sent_items, f) for f in os.listdir(sent_items) if not f.endswith('.ipynb_checkpoints')]
            emails = [f for f in emails if not f.endswith('clickathome')]
            outdir = os.path.join(out_root, os.path.split(acc)[1])
            os.makedirs(outdir, exist_ok=True)
            for email in emails:
                body = email_body(email)
                if len(body) > 500 and len(body) < 30000:
                    with open(os.path.join(outdir, str(count)), "w") as w:
                        w.write(body)
                        count += 1

def create_corpus(root, out):
    profiles = [os.path.join(root, f) for f in os.listdir(root)]
    for prof in profiles:
        emails = [os.path.join(prof, f) for f in os.listdir(prof)]
        if len(emails) < 60:
            continue
        outProfile = os.path.join(out, os.path.split(prof)[1])
        outTest = os.path.join(outProfile, 'test')
        outTrain = os.path.join(outProfile, 'train')
        os.makedirs(outTest, exist_ok=True)
        os.makedirs(outTrain, exist_ok=True)
        body = ''
        for email in emails:
            with open(email, "r") as r:
                body += r.read()
        offset = 0
        for i in range(0, 50):
            segment = body[offset:offset+500]
            offset += 500
            with open(os.path.join(outTrain, str(i)) + '.txt', "w") as f:
                f.write(segment)
        for i in range(0, 10):
            segment = body[offset:offset+500]
            offset += 500
            with open(os.path.join(outTest, str(i) + '.txt'), "w") as f:
                f.write(segment)
