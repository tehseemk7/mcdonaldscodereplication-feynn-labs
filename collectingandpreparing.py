import pandas as pd
data = pd.read_csv('mcdonalds.csv')
print(data.head())
print(data.isnull().sum())
data = data.dropna()

