from Profile import Profile
import numpy as np
import pandas as pd




class IdentProfile(Profile):
    def __init__(self, path, current_class, comparison = None, email_size = 350, ngram_size = [5,6], f = [1,2]):
        '''
        differs from Profile with argument current_class that corresponds to the classification label
        '''
        self.current_class = current_class
        self.path = path
        self.comparison = comparison
        self.email_size = email_size
        self.conj = self.functionWords(self.conj_path)
        self.quan = self.functionWords(self.quan_path)
        self.dete = self.functionWords(self.dete_path)
        self.prep = self.functionWords(self.prep_path)
        self.pron = self.functionWords(self.pron_path)
        self.aver = self.functionWords(self.aver_path)


    def create_profile(self):
        with open(self.path, 'r', encoding='ISO-8859-1') as r:
            text = r.read()
        
        df = self.extract(text, self.current_class)
        df = df.drop(0, axis=1)
        df.insert(0, 'target', self.current_class)
        return df

    def extract(self, text, classification):
        features = []
        for email in self.cut_email(text):
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
            tmp += self.punctuation(email)
            tmp.append(self.shortWords(words)/len(words))
            tmp.append(self.longWords(words)/len(words))
            tmp.append(self.func_word_type(words, self.conj)/len(words))
            tmp.append(self.func_word_type(words, self.quan)/len(words))
            tmp.append(self.func_word_type(words, self.dete)/len(words))
            tmp.append(self.func_word_type(words, self.prep)/len(words))
            tmp.append(self.func_word_type(words, self.pron)/len(words))
            tmp.append(self.func_word_type(words, self.aver)/len(words))
            tmp += self.countFuncWords(words, self.functionWords(self.all_words))
            """tmp.append(self.countFuncWords(words, self.functionWords(self.prepositions_path)))
            tmp.append(self.countFuncWords(words, self.functionWords(self.auxiliaryVerbs_path)))
            tmp.append(self.countFuncWords(words, self.functionWords(self.conjunctions_path)))
            tmp.append(self.countFuncWords(words, self.functionWords(self.quantifiers_path)))
            tmp.append(self.countFuncWords(words, self.functionWords(self.determiners_path)))"""
            features.append(tmp)
            print(tmp)
        df = pd.DataFrame(np.array(features))
        return df

        
class IdentText(Profile):
    def __init__(self, path, text, comparison=None, email_size=350, ngram_size = [5,6], f=[1,2]):
        self.path = path
        self.comparison = comparison
        self.email_size = email_size
        self.ngram_size = ngram_size
        self.f = f
        self.conj = self.functionWords(self.conj_path)
        self.quan = self.functionWords(self.quan_path)
        self.dete = self.functionWords(self.dete_path)
        self.prep = self.functionWords(self.prep_path)
        self.pron = self.functionWords(self.pron_path)
        self.aver = self.functionWords(self.aver_path)
        self.text = text
    
    def create_profile(self):
       return self.extract(self.text)

    def extract(self, text):
        features = []
        for email in self.cut_email(text):
            words = self.words(email)
            sents = self.sents(email)
            tmp = []
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
            tmp += self.punctuation(email)
            tmp.append(self.shortWords(words)/len(words))
            tmp.append(self.longWords(words)/len(words))
            tmp.append(self.func_word_type(words, self.conj)/len(words))
            tmp.append(self.func_word_type(words, self.quan)/len(words))
            tmp.append(self.func_word_type(words, self.dete)/len(words))
            tmp.append(self.func_word_type(words, self.prep)/len(words))
            tmp.append(self.func_word_type(words, self.pron)/len(words))
            tmp.append(self.func_word_type(words, self.aver)/len(words))
            tmp += self.countFuncWords(words, self.functionWords(self.all_words))
            features.append(tmp)
        df = pd.DataFrame(np.array(features))
        return df


