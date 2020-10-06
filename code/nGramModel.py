import numpy as np
import os
class nGramModel:
    def __init__(self, path, f, ngram_size, cut_size=500):
        """initializes the frequency and ngram size"""
        self.f = f
        self.cut_size = cut_size
        self.size = ngram_size
        self.path = path
        self.name = os.path.basename(path)
        self.other_users = [os.path.join(os.path.dirname(path), f) for f in os.listdir(os.path.dirname(path)) if f.endswith('.txt') and f != self.name]
        self.ngram_profile = self.profile_ngram()
        self.threshold = self.get_threshold()
        
    def block_ngram(self, email):
        unique = set()
        common = set()
        for i in range(self.size, len(email)):
            ngram = email[i-self.size:i]
            if ngram in unique:
                common.add(ngram)
            else:
                unique.add(ngram)
        all_ngrams = common.union(unique)
        unique.difference_update(common)
        return unique, all_ngrams
    
    def profile_ngram(self):
        ngrams = {}
        with open(self.path, 'r', encoding='ISO-8859-1') as r:
            all_emails = r.read()
        all_emails = all_emails[:len(all_emails)//2]
        for email in self.cut_email(all_emails):
            for i in  range(self.size, len(email)):
                ngram = email[i-self.size:i]
                if ngram in ngrams:
                    ngrams[ngram] += 1
                else:
                    ngrams[ngram] = 1
        ngram_set = set()    
        for key in ngrams:
            if ngrams[key] >= self.f or ngrams[key] == 1:
                ngram_set.add(key)
        return ngram_set
    
    def similarity(self, email):
        block_unique, block_all = self.block_ngram(email)
        numerator = len(block_unique.intersection(self.ngram_profile))
        r_m0 = numerator / len(block_unique)
        numerator = len(block_all.intersection(self.ngram_profile))
        r_m1 = numerator / len(block_unique)
        return r_m0, r_m1
    
    def get_threshold(self):
        """Sets the threshold"""
        with open(self.path, 'r', encoding='ISO-8859-1') as r:
            emails = r.read()
        emails = emails[len(emails)//2:]
        simil_m0 = [] # for only unique ngrams in the email block
        simil_m1 = [] # For all ngrams in the email block
        for email in self.cut_email(emails):
            m0, m1 = self.similarity(email)
            simil_m0.append(m0)
            simil_m1.append(m1)
        simil_m0 = np.array(simil_m0, dtype=np.double)
        simil_m1 = np.array(simil_m1, dtype=np.double)
        m0_thresh = self.calculate_threshold(simil_m0, 0)
        m1_thresh = self.calculate_threshold(simil_m1, 1)
        return m0_thresh, m1_thresh
    
    def calculate_threshold(self, simil, m):
        up = False
        down = False
        delta = 1
        threshold = np.mean(simil) - (np.var(simil) / 2)
        while delta > 0.0001:
            FAR, FRR = self.ngram_FAR_FRR(simil, threshold, m)
            if (FRR - FAR) > 0:
                down = True
                threshold -= delta
            elif (FRR -FAR) < 0:
                up = True
                threshold += delta
            else:
                return threshold
            if up and down:
                up = False
                down = False
                delta = delta/10
        return threshold
    
    def ngram_FAR_FRR(self, simil, threshold, m):
        tests, positive_count = self.get_tests()
        results = []
        for email in tests:
            if m == 0:
                r, _ = self.similarity(email)
            elif m == 1:
                _, r = self.similarity(email)
            results.append(r)
        positives = results[:positive_count]
        negatives = results[positive_count:]
        FR = 0
        FA = 0
        for p in positives:
            if p < threshold:
                FR += 1
        for n in negatives:
            if n >= threshold:
                FA += 1
        FRR = FR/len(positives)
        FAR = FA/len(negatives)
        return FAR, FRR
    
    def get_tests(self):
        tests = []
        with open(self.path, 'r', encoding='ISO-8859-1') as r:
            emails = r.read()
        emails = emails[len(emails)//2:]
        positives = 0 
        for email in self.cut_email(emails):
            tests.append(email)
            positives += 1
        for user in self.other_users:
            with open(user, 'r', encoding='ISO-8859-1') as r:
                emails = r.read()
            tests.append(emails[self.cut_size*3:self.cut_size*4])
        return tests, positives
    
    def decision(self, email):
        m0, m1 = self.similarity(email)
        if m0 >= self.threshold[0]:
            d0 = 1
        else:
            d0 = 0
        if m1 >= self.threshold[1]:
            d1 = 1
        else:
            d1 = 0
        return d0, d1
    
    def decision_similarity(self, email):
        m0, m1 = self.similarity(email)
        if m0 >= self.threshold[0]:
            d0 = 1
        else:
            d0 = 0
        if m1 >= self.threshold[1]:
            d1 = 1
        else:
            d1 = 0
        return m0, m1, d0, d1
    
    def cut_email(self, emails, start = 1):
        for i in range(self.cut_size * start, len(emails), self.cut_size):
            yield emails[i-self.cut_size:i]