import pandas as pd
import re
from process_twitter1 import clean_text

#import datasets
data = pd.read_csv(r"C:\Users\wyman\OneDrive\Desktop\Datasets\Tweets.csv")

#filter out data with less than 0.6 sentiment confidence
data = data[data['airline_sentiment_confidence'] > 0.6]
data = data[['airline_sentiment', 'text']]

cols = ['Sentiment', 'Text']
data.columns = [i for i in cols]

#clean up text
text_clean = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"

text = data['Text'].apply(lambda x: clean_text(x))

#processed dataframe to csv
data = pd.DataFrame({'Sentiment': data['Sentiment'],
                    'Text': text})

data.to_csv(r'C:\Users\wyman\OneDrive\Desktop\Datasets\processed_data\twitter3.csv')