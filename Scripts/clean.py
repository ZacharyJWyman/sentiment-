import pandas as pd
import numpy as np
from nltk.stem import SnowballStemmer
import re

data = pd.read_csv(r'C:\Users\wyman\OneDrive\Desktop\sentiment_tw\2477_4140_compressed_training.1600000.processed.noemoticon.csv.zip',
encoding = 'latin', header = None)

cols = ['Target', 'id', 'date', 'query', 'person', 'Text']
data.columns = [i for i in cols]
data = data[['Target', 'Text']]

label_dict = {0: 'negative',
             4: 'positive'}

def apply_labels(label):
        return label_dict[label]
data['Target'] = data['Target'].apply(lambda x: apply_labels(x))

text_clean = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"

def clean_text(text, stem=True):
    text = re.sub(text_clean, ' ', str(text).lower()).strip()
    return text

data['Text'].apply(lambda x: clean_text(x))