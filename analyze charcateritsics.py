from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
data['yummy'] = label_encoder.fit_transform(data['yummy'])
data['convenient'] = label_encoder.fit_transform(data['convenient'])
data['spicy'] = label_encoder.fit_transform(data['spicy'])
sns.pairplot(data, hue='cluster', vars=['yummy', 'convenient', 'spicy'])
plt.title('Cluster Pair Plot')
plt.show()