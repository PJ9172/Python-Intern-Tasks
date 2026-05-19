from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# 1. Generate "Moon" shaped data (impossible for K-Means)
X, y = make_moons(n_samples=300, noise=0.05, random_state=42)

# 2. Scaling is always a good idea for distance-based models
X = StandardScaler().fit_transform(X)

# 3. Apply DBSCAN
# eps: the radius, min_samples: the MinPts
dbscan = DBSCAN(eps=0.3, min_samples=5)
clusters = dbscan.fit_predict(X)

# 4. Plot the results
plt.scatter(X[:, 0], X[:, 1], c=clusters, cmap='viridis')
plt.title("DBSCAN: Finding Non-Spherical Clusters")
plt.show()