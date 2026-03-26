import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Sample documents
documents = [
    "Machine learning is part of artificial intelligence",
    "Deep learning belongs to machine learning",
    "Artificial intelligence is changing technology",
    "Python is a famous programming language",
    "Java and Python are commonly used languages",
    "Software developers write programs using languages",
    "Data science uses machine learning methods",
    "Programming languages help to build software",
    "AI and ML are modern technologies",
    "Developers create applications using Python"
]

# Create DataFrame
data = pd.DataFrame({"Text": documents})
print("Dataset:\n")
print(data)

# TF-IDF vectorization
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(data["Text"])
print("\nTF-IDF matrix shape:", X.shape)

# K-Means clustering
model = KMeans(n_clusters=3, random_state=1)
model.fit(X)
data["Cluster"] = model.labels_

print("\nClustered Documents:\n")
print(data)

# PCA for 2D visualization
pca = PCA(n_components=2)
points = pca.fit_transform(X.toarray())

# Plot clusters
plt.figure(figsize=(8,6))
plt.scatter(points[:,0], points[:,1], c=data["Cluster"], cmap='viridis', s=100)
plt.title("K-Means Text Clustering")
plt.xlabel("Component 1")
plt.ylabel("Component 2")
plt.colorbar(label="Cluster")
plt.show()