import re
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import pickle
from keras.models import load_model

#convert numpy array to sentiment 
label_dict = {2: 'positive',
           1: 'neutral',
           0:'negative'}

def clean_text(text, stem=False):
    text_clean = '@\S+|https?:\S|[^A-Za-z0-9]+'
    text = re.sub(text_clean, ' ', str(text).lower()).strip()
    #text = tf.strings.substr(text, 0, 300) #restrict text size to 300 chars
    return text

def tokenize_text(text):
    #load tokenizer obj
    with open(r"C:\Users\19712\OneDrive\Desktop\sent_clone\sentiment-\model\tokenizer.pickle", 'rb') as handle:
        tokenizer = pickle.load(handle)
    return tokenizer

def padding(text, tokenizer):
    text = pad_sequences(tokenizer.texts_to_sequences(text), maxlen = 500) #len is number of words
    if isinstance(text, str):
        text = [text]
    return text

def apply_labels(label):
    return label_dict[label]

def classify_sentiment(text):
    score = loaded_model.predict(padded_text)
    y_pred = np.argmax(score, axis = 1).reshape(-1,1)
    y_sentiment = np.vectorize(label_dict.get)(y_pred)
    return y_pred, y_sentiment