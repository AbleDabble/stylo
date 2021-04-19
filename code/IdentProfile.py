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
        df = self.extract(self.path,self.current_class)
        return df
        

