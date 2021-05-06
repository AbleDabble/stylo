import tensorflow as tf
import os
import pandas as pd
import numpy as np
import pickle as pkl
import sys
from contextlib import contextmanager

def print_progress(stage, message, num_stages=4):
    out = '[' + '=' * stage + ' ' * (num_stages - stage) + '] ' + message
    print(' ' * 80, end='\r')
    if stage != num_stages: print(out, end='\r')
    else: print(out)



@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout


class Personality:
    def __init__(self):
        # Deduction Subjective: N = 0, S = 1
        # Deduction Objective: I = 0, E = 1
        # Induction Subjective: F = 0, T = 1
        # Induction Objective = P = 0, J = 1
        self.ds_conversion = ['N', 'S']
        self.do_conversion = ['I', 'E']
        self.is_conversion = ['F', 'T']
        self.io_conversion = ['P', 'J']

        with open('../models/tokenizer.tf', 'rb') as f:
            self.tokenizer = pkl.load(f)

        print_progress(0, 'Loading Deduction Subjective Model')
        with suppress_stdout():
            self.ds = tf.keras.models.load_model('../models/ds')
        print_progress(1, 'Loading Deduction Objective Model')
        with suppress_stdout():
            self.do = tf.keras.models.load_model('../models/do')
        print_progress(2, 'Loading Induction Subjective Model')
        with suppress_stdout():
            self.isu = tf.keras.models.load_model('../models/is')
        print_progress(3, 'Loading Induction Objective Model')
        with suppress_stdout():
            self.io = tf.keras.models.load_model('../models/io')
        print_progress(4, 'Done')

    def predict(self, text):
        text = [text] # need to wrap text into array
        tokenized = self.tokenizer.texts_to_sequences(text)
        tokenized = tf.keras.preprocessing.sequence.pad_sequences(tokenized, maxlen=1883, padding='post')
        tokenized = np.array(tokenized)
        with suppress_stdout():
            ds_result = self.ds.predict(tokenized)
            do_result = self.do.predict(tokenized)
            is_result = self.isu.predict(tokenized)
            io_result = self.io.predict(tokenized)
        result = ''
        print(ds_result)
        print(do_result)
        print(is_result)
        print(io_result)
        # convert to binary values
        if do_result < 0.5:
            result += 'I'
        else:
            result += 'E'
        if ds_result < 0.5:
            result += 'N'
        else:
            result += 'S'
        if is_result < 0.5:
            result += 'F'
        else:
            result += 'T'
        if io_result < 0.5:
            result += 'P'
        else:
            result += 'J'
        return result


