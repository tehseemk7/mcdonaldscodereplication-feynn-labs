import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('mcdonalds.csv')


data.columns = data.columns.str.strip()


if 'cluster' not in data.columns:
    raise KeyError("'cluster' column is missing from the DataFrame")


numeric_columns = data.select_dtypes(include=['number']).columns.tolist()
if 'cluster' not in numeric_columns:
    numeric_columns.append('cluster')


data_numeric = data[numeric_columns]

print(data_numeric['cluster'].isnull().sum())


data_numeric = data_numeric.reset_index(drop=True)


print(data_numeric['cluster'].shape)
print(data_numeric['cluster'].head())


profile = data_numeric.groupby('cluster').mean()


profile.plot(kind='bar', figsize=(12, 8))
plt.title('Segment Profile Plot')
plt.xlabel('Cluster')
plt.ylabel('Value')
plt.show()