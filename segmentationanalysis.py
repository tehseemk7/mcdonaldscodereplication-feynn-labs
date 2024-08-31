import sys
sys.path.append("C:/Users/tehse/AppData/Roaming/Python/Python312/site-packages")
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
data = pd.read_csv('mcdonalds.csv') 
features = pd.get_dummies(data[['yummy', 'convenient', 'spicy']], drop_first=True)
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

kmeans = KMeans(n_clusters=4, random_state=0)  
data['cluster'] = kmeans.fit_predict(scaled_features)
print(pd.DataFrame(kmeans.cluster_centers_, columns=['yummy', 'convenient', 'spicy']))

