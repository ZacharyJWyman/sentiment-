import pandas as pd
import re

#import datasets
negative = pd.read_csv(r"C:\Users\wyman\OneDrive\Desktop\Datasets\processedNegative.csv",
                      header = None)
neutral = pd.read_csv(r"C:\Users\wyman\OneDrive\Desktop\Datasets\processedNeutral.csv",
                     header = None)
positive = pd.read_csv(r"C:\Users\wyman\OneDrive\Desktop\Datasets\processedPositive.csv",
                      header = None)

#transpose datasets
negative = negative.T
neutral = neutral.T
positive = positive.T

#rename and add sentiment to respective df
dfs = [negative, neutral, positive]
cols = ['Text']
sentiment = ['negative', 'neutral', 'positive']

j = 0
for df in dfs:
    df.columns = [i for i in cols]
    df['Sentiment'] = sentiment[j]
    j+=1
  
#merge into one dataframe 
data = pd.concat([negative, neutral, positive], axis = 0)

#clean up text
text_clean = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"

#apply function 
def clean_text(text, stem=False):
    text = re.sub(text_clean, ' ', str(text).lower()).strip()
    return text

text = data['Text'].apply(lambda x: clean_text(x))

#processed dataframe to csv
data = pd.DataFrame({'Sentiment': data['Sentiment'],
                    'Text': text})

data.to_csv(r'C:\Users\wyman\OneDrive\Desktop\Datasets\processed_data\twitter1.csv')
