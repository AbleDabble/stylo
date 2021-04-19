from Profile import Profile
import numpy as np
import pandas as pd




class IdentProfile(Profile):
    def __init__(self, path, comparison = None, email_size = 350, ngram_size = [5,6], f = [1,2], current_class=0):
        '''
        differs from Profile with argument current_class that corresponds to the classification label
        '''
        super().__init__(path, comparison, email_size, ngram_size, f)
        self.current_class = current_class

    def create_profile(self):
        df = self.extract_positives()
        target = np.fill(len(df), self.current_class)
        df = df.drop(0, axis=1)
        target = pd.Series(target)
        df.insert(0, 'target', target)
        return df
        
class IdentText(Profile):
    def __init__(self, path, text, comparison=None, email_size=350, ngram_size = [5,6], f=[1,2]):
        
        super().__init__(path, comparison, email_size, ngram_size, f)
        self.text = text
    
    def create_profile(self):
        df = self.extract(self.text, 9999)
        return df
