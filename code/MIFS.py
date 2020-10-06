import numpy as np
import pandas
from sklearn.feature_selection import mutual_info_classif

class MIFS:
    """A feature selection class based on the mutual information of a feature"""
    def __init__(self, low=0, high=95):
        self.low = low
        self.high = high
    
    def MI(self, x, y):
        """Returns mutual information for every feature in dataframe as a dictionary in format: {Feature:mutual_information}"""
        return dict(zip([i for i in range(0,len(x))], mutual_info_classif(x, y, random_state=2)))
    
    def ensure_numpy(self, *args):
        """
        Makes sure the passed dataframes are converted to numpy arrays if they are not already. Also checks to make
        passed df's are either ndarrays or pandas DataFrames and if they aren't raises an exception
        """
        npdarrays = []
        for arg in args:
            if not isinstance(arg,(pandas.core.frame.DataFrame, np.ndarray)):
                raise Exception("Wrong type", type(arg))
            elif isinstance(arg,pandas.core.frame.DataFrame):
                npdarrays.append(arg.to_numpy())
            else:
                npdarrays.append(arg)
        if len(npdarrays) > 1:
            return npdarrays
        else:
            return npdarrays[0]
    
    def fit(self, x, y):
        """finds which features to removed based on the low and high cutoff points"""
        mutual_info = self.MI(x, y)
        #print(mutual_info)
        self.features_to_remove = [int(attr) for attr in mutual_info if mutual_info[attr] <= self.low or mutual_info[attr] >= self.high]
        #print(self.features_to_remove)
    
    def transform(self, x):
        """Removes the selected features and returns the resulting array"""
        x_np = self.ensure_numpy(x)
        return np.delete(x_np, self.features_to_remove, axis=1)
    
    def fit_transform(self, x, y):
        self.fit(x, y)
        return self.transform(x)
        