import numpy as np

from transformers import pipeline

import torch

def bertweet(data):
    specific_model = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")
    result = specific_model(data)
    label = result[0]['label']
    score = result[0]['score']

    return label, score 

def roberta(data):
    specific_model = pipeline(model="cardiffnlp/twitter-roberta-base-sentiment")
    result = specific_model(data)
    label = result[0]['label']
    score = result[0]['score']

    if(label == 'LABEL_0'):
        label = 'Negative'
    elif(label == 'LABEL_1'):
        label = 'Neutral'
    else:
        label = 'Positive'

    return label, score 

def getSent(data, model):
    if(model == 'Bertweet'):
        label,score = bertweet(data)
        
    elif(model == 'Roberta'):
        label,score = roberta(data)