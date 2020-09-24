#script iterates through each juror and gives them 10 seconds to speak. Transcribes speech to text so that it can be implemented for NLP
#to predict sentiment of each juror towards specific topics.

import speech_recognition as sr
import pyaudio

jurors = ['nat', 'jon', 'dil', 'car']
storage = []

while len(storage) < len(jurors):
    print('Juror' + ' ' + jurors[len(storage)] + ' ' + 'is speaking:')
    init_rec = sr.Recognizer()
    with sr.Microphone() as source:
        audio_data = init_rec.record(source, duration=5) #each juror speaks for 10 seconds
        text = init_rec.recognize_google(audio_data)
        print('End of juror' + ' ' + jurors[len(storage)] + ' ' + 'speech')
        storage.append(text)
