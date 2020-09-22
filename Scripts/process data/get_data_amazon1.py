import pandas as pd
import gzip

#read large file (8 mil)
def parse(path):
  g = gzip.open(path, 'rb')
  for l in g:
    yield eval(l)

def getDF(path):
  i = 0
  df = {}
  for d in parse(path):
    df[i] = d
    i += 1
  return pd.DataFrame.from_dict(df, orient='index')
   
df = getDF(r"C:\Users\wyman\OneDrive\Desktop\Datasets\reviews_Books_5.json.gz")
#%%
data = df[['reviewText', 'overall', 'summary']]
data.to_csv(r'C:\Users\wyman\OneDrive\Desktop\Datasets\amazon.csv')
#%%

#condense file (4.5 mil)
data = pd.read_csv(r'C:\Users\wyman\OneDrive\Desktop\Datasets\amazon.csv')

data = data.sample(frac=0.05, replace = False, random_state = 42)
data = data[['reviewText', 'overall']]
data.to_csv(r'C:\Users\wyman\OneDrive\Desktop\Datasets\amazon.csv')