from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
new_data['cheap'] = le.fit_transform(new_data['cheap'])
new_data['tasty'] = le.fit_transform(new_data['tasty'])
new_data['expensive'] = le.fit_transform(new_data['expensive'])
new_features = new_data[['cheap', 'tasty', 'expensive']]
scaler.fit(new_features)
new_scaled_features = scaler.transform(new_features)
new_clusters = kmeans.predict(new_scaled_features)
new_data['cluster'] = new_clusters
new_profile = new_data.groupby('cluster').apply(lambda x: x.mode().iloc[0])
print(new_profile)

plt.figure(figsize=(12, 8))
new_profile.plot(kind='bar', position=0, label='New Profile')
new_profile.plot(kind='bar', position=0, label='New Profile')
plt.title('Comparison of Old and New Segment Profiles')
plt.xlabel('Cluster')
plt.ylabel('Mean Value')
plt.legend()
plt.show()