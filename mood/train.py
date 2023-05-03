import os
import pandas as pd
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dropout, Bidirectional, Dense, Embedding
from tensorflow.keras.layers import TextVectorization

# df = pd.read_csv("./data/train.csv")
# test_df = pd.read_csv('data/test.csv')
df = pd.read_csv("/home/tdramos32/Programs/Ment-Care/mood/data/train.csv")
test_df = pd.read_csv('/home/tdramos32/Programs/Ment-Care/mood/data/test.csv')

MAX_FEATURES = 200000 #no. of words in vocab
X = df['comment_text']
y = df[df.columns[2:]].values

vectorizer = TextVectorization(max_tokens=MAX_FEATURES,
                               output_sequence_length=1800,
                               output_mode='int')
vectorizer.adapt(X.values)


model = tf.keras.models.load_model('/home/tdramos32/Programs/Ment-Care/mood/toxicity.h5')

def score_comment(comment):
    vectorized_comment = vectorizer([comment])
    results = model.predict(vectorized_comment)
    
    text = ''
    for idx, col in enumerate(df.columns[2:]):
        text += '{}: {}\n'.format(col, results[0][idx]>0.5)
    
    return text

def clean_output(comment):
    output = score_comment(comment)
    result_list = []
    word = ""
    for out in output:
 
        if out == '\n':
            result_list.append(word)
            word = ""
            continue
        word = word+out

    answers = {}
    for i in range(len(result_list)):
        arr = result_list[i].split(": ")
        
        answers[arr[0]] = arr[1]
         
    return answers
