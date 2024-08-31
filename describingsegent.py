import statsmodels.api as sm
from statsmodels.graphics.mosaicplot import mosaic
import matplotlib.pyplot as plt
contingency_table = pd.crosstab(data['Like'], data['Age'])
contingency_table = contingency_table.reset_index()
contingency_table.columns = ['Like'] + [str(col) for col in contingency_table.columns[1:]]
mosaic(contingency_table, title='Mosaic Plot of Segment Membership and Liking McDonald\'s')
plt.show()

sns.boxplot(x='Like', y='Age', data=data)
plt.title('Age Distribution by Segment')
plt.xlabel('Like')
plt.ylabel('Age')
plt.show()