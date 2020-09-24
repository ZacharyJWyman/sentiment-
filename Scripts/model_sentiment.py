#script that preprocesses text for model prediction

#import required libraries
import pandas as pd
import numpy as np
import tensorflow as tf
import re
from keras.models import load_model
from helperFunctions import *

#load model
loaded_model = load_model(r'C:\Users\19712\my_model')

#data for test purposes 
data = pd.read_csv(r"C:\Users\19712\OneDrive\Desktop\NLP\merged_data.csv")
data.drop('Unnamed: 0', axis = 1, inplace = True)

X_train_pipe = data['Text'][10000:10500]
X_test_pipe = data['Text'][2000:2100]

#prepare text for model input
text = X_test_pipe.apply(lambda x: clean_text(x))
tokenizer = tokenize_text(text)
X_test_pipe = padding(text, tokenizer)

#predictions
loaded_score = loaded_model.predict(X_test_pipe)
y_loaded_pred = np.argmax(loaded_score, axis = 1).reshape(-1,1)

#convert numpy array to sentiment 
label_dict = {2: 'positive',
           1: 'neutral',
           0:'negative'}

y_sentiment = np.vectorize(label_dict.get)(y_loaded_pred)