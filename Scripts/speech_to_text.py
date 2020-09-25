#script iterates through each juror and gives them 10 seconds to speak. Transcribes speech to text so that it can be implemented for NLP
#to predict sentiment of each juror towards specific topics.

import speech_recognition as sr
import pyaudio
import pandas as pd
from helperFunctions import *

jurors = ['Zack', 'Ben']
storage = []
storage_df = pd.DataFrame()


while len(storage) < len(jurors):
    print('Juror' + ' ' + jurors[len(storage)] + ' ' + 'is speaking:')
    init_rec = sr.Recognizer()
    with sr.Microphone() as source:
        audio_data = init_rec.adjust_for_ambient_noise(source)
        audio_data = init_rec.listen(source) #each juror speaks for 10 seconds
        audio_text = init_rec.recognize_google(audio_data)
        print('End of juror' + ' ' + jurors[len(storage)] + ' ' + 'speech')
        storage.append(audio_text)
        cleaned = clean_text(audio_text)
        tokenized = tokenize_text(cleaned)
        padded_text = padding(cleaned, tokenized) #fix padded text elongating rows
        
