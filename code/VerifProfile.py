from Profile import Profile
import numpy as np
import pandas as pd




class VerifProfile(Profile):
    def __init__(self, path, comparison: str, email_size = 350, ngram_size = [5,6], f = [1,2]):
        super().__init__(path, comparison, email_size, ngram_size, f)
        self.comparison = comparison
    
    def create_profile(self):
        # Create create csv for user
        with open(self.path, 'r', encoding='ISO-8859-1') as r:
            comments = r.read()
        
        # Format Profile CSV to include label for target
        profile_csv = self.extract_all(comments)
        target = profile_csv[[0]].copy().astype('int32')
        profile_csv = profile_csv.drop(0, axis=1)
        profile_csv.insert(0, 'target', target)

        # Create The comparison user
        with open(self.comparison, 'r', encoding='ISO-8859-1') as r:
            comments = r.read()

        comparison_csv = self.extract(comments, 0)
        comparison_csv = comparison_csv.drop(0, axis=1)
        return profile_csv, comparison_csv

