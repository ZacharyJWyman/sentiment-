#script iterates through each juror. Transcribes speech to text so that it can be implemented for NLP
#to predict sentiment of each juror towards specific topics.

import speech_recognition as sr
import pyaudio
import pandas as pd
from helperFunctions import *
import numpy as np

#load model
loaded_model = load_model(r'C:\Users\19712\my_model')


#transcribes speech to text
jurors = ['Zack', 'Ben']
storage = []


while len(storage) < len(jurors):
    print('Juror' + ' ' + jurors[len(storage)] + ' ' + 'is speaking:')
    init_rec = sr.Recognizer()
    with sr.Microphone() as source:
        audio_string = []
        audio_data = init_rec.adjust_for_ambient_noise(source)
        audio_data = init_rec.listen(source) #each juror speaks for 10 seconds
        audio_text = init_rec.recognize_google(audio_data)
        print('End of juror' + ' ' + jurors[len(storage)] + ' ' + 'speech')
      
        #storage of all spoken text (maybe convert to dict for key, value with juror name)
        storage.append(audio_text)
        audio_string.append(audio_text)
       
        #funtions
        cleaned = clean_text(audio_string)
        tokenized = tokenize_text(audio_string)
        padded_text = padding(audio_string, tokenized) #fix padded text elongating rows
        
        #sentiment
        loaded_score = loaded_model.predict(padded_text)
        y_loaded_pred = np.argmax(loaded_score, axis = 1).reshape(-1,1)
        y_sentiment = np.vectorize(label_dict.get)(y_loaded_pred)
        
