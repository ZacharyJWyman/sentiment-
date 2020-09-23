import pandas as pd

#gather data and clean
data = pd.read_csv(r'C:\Users\wyman\OneDrive\Desktop\Datasets\amazon.csv')
data.drop('Unnamed: 0', axis = 1, inplace = True)

#remame cols to be consistent
cols = ['Text', 'Sentiment']
data.columns = [i for i in cols]
data = data[(data['Sentiment'] != 2) & (data['Sentiment'] != 4)]
data['Sentiment'] = data['Sentiment'].astype(int)

#rename numeric to negative, neutral, positive classes 
label_dict = {1: 'negative',
              3: 'neutral',
              5: 'positive'}

def apply_labels(label):
    return label_dict[label]
data['Sentiment'] = data['Sentiment'].apply(lambda x: apply_labels(x))


