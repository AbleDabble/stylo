import re
from nltk.corpus import PlaintextCorpusReader
from nltk.stem.porter import PorterStemmer
import numpy as np
import os
from itertools import groupby
import pandas as pd
import csv
from sklearn.preprocessing import MinMaxScaler
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from mdlp.discretization import MDLP
from imblearn.over_sampling import RandomOverSampler
from imblearn.over_sampling import SMOTE
from EntropyDiscretization import EntropyDiscretization
from nGramModel import nGramModel

class Profile:
    all_words = '../dependencies/allWords.txt'
    conj_path = '../dependencies/Conjunctions.txt'
    quan_path = '../dependencies/Quantifiers.txt'
    dete_path = '../dependencies/Determiners.txt'
    prep_path = '../dependencies/Prepositions.txt'
    pron_path = '../dependencies/Pronouns.txt'
    aver_path = '../dependencies/AuxiliaryVerbs.txt'
    def __init__(self, path, email_size = 500, ngram_size = [6], f = [4]):
        """Initializes a profile, and initailizes the ngram model based on tuples based to ngram_size and f.
        The tuples passed should be of the same size and their positions are respective of each other, that is 
        ngram_size of (5,6), and f of (1,2) will create two ngram models one with ngram size 5 and f of 1, and
        one with ngram size 6 and f of 2."""
        
        self.email_size = email_size
        
        if len(ngram_size) != len(f):
            raise Exception("the length of ngram size must be equal to the length of f")
        self.ngram_models = []
        for i in range(0, len(ngram_size)):
            self.ngram_models.append(nGramModel(path, f[i], ngram_size[i], cut_size=self.email_size))
        self.path = path
        self.f = f
        self.path = path
        self.name = os.path.basename(path)
        self.other_users = [os.path.join(os.path.dirname(path), f) for f in os.listdir(os.path.dirname(path)) if f.endswith('.txt') and f != self.name]
        #self.other_test_users = [os.path.join(os.path.dirname(test_path), f) for f in os.listdir(os.path.dirname(test_path)) if f.endswith('.txt') and f != self.name]
        self.conj = self.functionWords(self.conj_path)
        self.quan = self.functionWords(self.quan_path)
        self.dete = self.functionWords(self.dete_path)
        self.prep = self.functionWords(self.prep_path)
        self.pron = self.functionWords(self.pron_path)
        self.aver = self.functionWords(self.aver_path)
    
    # =========== GET WORDS AND SENTS =============
    
    def sents(self, email):
        return sent_tokenize(email)
    
    def words(self, email):
        return word_tokenize(email)
    
    def cut_email(self, emails, start = 1):
        for i in range(self.email_size * start, len(emails), self.email_size):
            yield emails[i-self.email_size:i]
    
    # ==================== END ====================
    
    # ================== Features =================
    def avgWordLen(self, words):
        s = sum(len(word) for word in words) / len(words)
        return s
    def avgSentLen(self, sents):
        s = sum(len(sent) for sent in sents) / len(sents)
        return s
    def avgSentLenByWord(self, sents):
        count = 0
        for sent in sents:
            count += len(word_tokenize(sent))
        return count / len(sents)
    def yules(self, words):
        d = {}
        stemmer = PorterStemmer()
        for word in words:
            word = stemmer.stem(word).lower()
            try:
                d[word] += 1
            except KeyError:
                d[word] = 1
        M1 = float(len(d))
        M2 = sum([len(list(g)) * (freq**2) for freq, g, in groupby(sorted(d.values()))])
        if M1 != M2:
            yules = (M1*M2)/(M2-M1)
        else:
            yules = 0
        return yules
    def vocab_richness(self, words):
        return len(set(words))/len(words)
    def numWords(self, words):
        return len(words)
    def numSents(self, sents):
        return len(sents)
    def legomena(self, words):
        d = {}
        for word in words:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
        hapax = sum(d[word] for word in d if d[word] == 1)
        dis = sum(d[word] for word in d if d[word] == 2) / 2
        return hapax, dis
    def specialCharacters(self, email):
        return len(re.findall('[\[\]<>{}#$@%&*]', email))
    def vowels(self, email):
        return len(re.findall('[aeiou]', email))
    def punctuation(self, email):
        return len(re.findall('[.,\'?":!]', email))
    def shortWords(self, words):
        return sum(1 for word in words if len(word) <=3)
    def longWords(self, words):
        return sum(1 for word in words if len(word) > 6)
    def functionWords(self, path):
        with open(path, 'r', encoding='ISO-8859-1') as r:
            c = r.read()
        return set([word for word in c.splitlines() if '/' not in word])
    def func_word_type(self, words, funcWords):
        """Returns the total count of all function words passed to function"""
        return sum(1 if word in funcWords else 0 for word in words)
        pass
    
    def ngram_dec_sim(self, email):
        """Returns the decision and similarity for both modes of calculation for all ngram models included in the profile"""
        dec_sim = []
        for model in self.ngram_models:
            dec_sim += model.decision_similarity(email)
        return dec_sim
    
    # ==================== END ====================
    
    def extract_all(self, training = True):
        if training:
            path = self.path
            users = self.other_users
        else:
            path = self.test_path
            users = self.other_test_users
        with open(path, 'r', encoding='ISO-8859-1') as r:
            emails = r.read()
        df = self.extract(emails, 1)
        for user in users:
            with open(user, 'r', encoding='ISO-8859-1') as r:
                emails = r.read()
            tmp_df = self.extract(emails, 0)
            df = df.append(tmp_df, ignore_index = True)
        return df
    def create_profile(self):
        # Remove target (y) from the dataframe
        df = self.extract_all()
        #tf = self.extract_all(training=False)
        target = df[[0]]
        target = target.copy()
        target = target.astype('int32')
        df = df.drop(0, axis=1)
        
        # Do for test frame
        """test_target = tf[[0]]
        test_target = test_target.copy()
        test_target = test_target.astype('int32')
        tf = tf.drop(0, axis=1)"""
        
        # Scale data with min max normalization
        self.scaler = MinMaxScaler()
        self.scaler.fit(df)
        df = self.scaler.transform(df)
        df = pd.DataFrame(df)
        #tf = scaler.transform(tf) # scale test frame
        # Oversample minority case
        # sm = SMOTE(random_state=0)
        # x_resampled, y_resampled = sm.fit_resample(df, target)
        # ros = RandomOverSampler(random_state = 0)
        #x_resampled, y_resampled = ros.fit_resample(df, target)
        # transform dataset with mdlp
        #discretizer = EntropyDiscretization()
        #conv_x = discretizer.fit_transform(df.to_numpy(), target.to_numpy())
        #test_conv_x = discretizer.transform(tf)
        
        df = pd.DataFrame(df)
        df.insert(0, "target", target)
        
        #tf = pd.DataFrame(tf)
        #tf.insert(0, "target", test_target)
        
        return df
    
    def create_test(self, path):
        """Creates the test csv from the path provided"""
        other_users = [os.path.join(os.path.dirname(path), f) for f in os.listdir(os.path.dirname(path)) if f.endswith('.txt') and f != self.name]
        with open(path, 'r', encoding='ISO-8859-1') as r:
            emails = r.read()
        df = self.extract(emails, 1)
        for user in other_users:
            with open(user, 'r', encoding='ISO-8859-1') as r:
                emails = r.read()
            tmp_df = self.extract(emails, 0)
            df = df.append(tmp_df, ignore_index = True)
        target = df[[0]]
        target = target.copy()
        target = target.astype('int32')
        df = df.drop(0, axis=1)
        df = self.scaler.transform(df)
        df = pd.DataFrame(df)
        df.insert(0, "target", target)
        return df
    
    def extract(self, emails, classification):
        features = []
        for email in self.cut_email(emails):
            words = self.words(email)
            sents = self.sents(email)
            tmp = []
            tmp.append(classification)
            tmp.append(self.avgWordLen(words))
            tmp.append(self.avgSentLen(sents))
            tmp.append(self.avgSentLenByWord(sents))
            tmp.append(self.yules(words))
            tmp.append(self.vocab_richness(words))
            tmp.append(self.numWords(words))
            tmp.append(self.numSents(sents))
            hapax, dis = self.legomena(words)
            tmp.append(hapax)
            tmp.append(dis)
            tmp.append(self.specialCharacters(email))
            tmp.append(self.vowels(email))
            tmp.append(self.punctuation(email))
            tmp.append(self.shortWords(words)/len(words))
            tmp.append(self.longWords(words)/len(words))
            tmp.append(self.func_word_type(words, self.conj)/len(words))
            tmp.append(self.func_word_type(words, self.quan)/len(words))
            tmp.append(self.func_word_type(words, self.dete)/len(words))
            tmp.append(self.func_word_type(words, self.prep)/len(words))
            tmp.append(self.func_word_type(words, self.pron)/len(words))
            tmp.append(self.func_word_type(words, self.aver)/len(words))
            tmp += self.countFuncWords(words, self.functionWords(self.all_words))
            tmp += self.ngram_dec_sim(email)
            """tmp.append(self.countFuncWords(words, self.functionWords(self.prepositions_path)))
            tmp.append(self.countFuncWords(words, self.functionWords(self.auxiliaryVerbs_path)))
            tmp.append(self.countFuncWords(words, self.functionWords(self.conjunctions_path)))
            tmp.append(self.countFuncWords(words, self.functionWords(self.quantifiers_path)))
            tmp.append(self.countFuncWords(words, self.functionWords(self.determiners_path)))"""
            features.append(tmp)
        df = pd.DataFrame(np.array(features), columns = range(0, len(features[0])))
        return df
    
    def countFuncWords(self, words, funcWords):
        d = {}
        for word in funcWords:
            d[word] = 0
        count = []
        for word in words:
            if word in funcWords:
                d[word] += 1
        for word in sorted(d.keys()):
            count.append(d[word])
        return count
    def tryint(self, s):
        """Converts the passed value into an into"""
        try:
            return int(s)
        except ValueError:
            return s
    def alphanum_key(self, s):
        """Createas a list of ints so the file can be sorted that way"""
        return [self.tryint(c) for c in re.split('([0-9]+)', s)]

    def sort_num(self, l):
        l.sort(key=self.alphanum_key)