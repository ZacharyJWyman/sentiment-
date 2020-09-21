import pandas as pd
import re
from process_twitter1 import clean_text #import function 

data = pd.read_csv(r'C:\Users\wyman\OneDrive\Desktop\sentiment_tw\2477_4140_compressed_training.1600000.processed.noemoticon.csv.zip',
                  encoding = 'latin', header = None)

cols = ['Target', 'id', 'date', 'query', 'person', 'Text']
data.columns = [i for i in cols]
data = data[['Target', 'Text']]

label_dict = {0: 'negative',
             4: 'positive'}

def apply_labels(label):
    return label_dict[label]
data.Target = data.Target.apply(lambda x: apply_labels(x))

#clean up text
text_clean = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"
text = data['Text'].apply(lambda x: clean_text(x))

data = pd.DataFrame({'Sentiment': data['Target'],
                       'Text': text})
