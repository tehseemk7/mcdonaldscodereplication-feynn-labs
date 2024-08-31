import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('mcdonalds.csv')
numerical_cols = data.select_dtypes(include=['int64', 'float64']).columns
data_numerical = data[numerical_cols]
corr_matrix = data_numerical.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
print(data_numerical.describe())
print(data.describe())
sns.histplot(data['Age'], kde=True)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
plt.figure(figsize=(10, 8))
plt.title('Correlation Heatmap')
plt.show()

