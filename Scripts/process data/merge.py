import pandas as pd

#read csv
path = r"C:\Users\wyman\OneDrive\Desktop\sentiment_clone\sentiment-\data\\"
df1 = pd.read_csv(path + 'amazon.csv')
df2 = pd.read_csv(path + 'twitter1.csv')
df3 = pd.read_csv(path + 'twitter2.csv')
df4 = pd.read_csv(path + 'twitter3.csv')
#%%
dfs = [df1, df2, df3, df4]
for df in dfs:
    df.drop('Unnamed: 0', axis = 1, inplace = True)
#%%
df2 = df2[['Sentiment', 'Text']]

data = pd.concat([df1, df2, df4], axis = 0)
#%%
data.to_csv(path + 'merged_data.csv')