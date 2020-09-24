import re
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

def clean_text(text, stem=False):
    text_clean = '@\S+|https?:\S|[^A-Za-z0-9]+'
    text = re.sub(text_clean, ' ', str(text).lower()).strip()
    #text = tf.strings.substr(text, 0, 300) #restrict text size to 300 chars
    return text

def tokenize_text(text):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(text)
    return tokenizer

def padding(text, tokenizer):
    text = pad_sequences(tokenizer.texts_to_sequences(text), 
                       maxlen = 500)
    return text

def apply_labels(label):
    return label_dict[label]