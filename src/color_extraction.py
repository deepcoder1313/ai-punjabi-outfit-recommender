import cv2
import numpy as np
from sklearn.cluster import KMeans

def extract_dominant_color(image_path, k=3):
    img = cv2.imread(image_path)

    if img is None:
        raise ValueError("Image not found or path is wrong")

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img.reshape((-1, 3))

    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(img)

    colors = kmeans.cluster_centers_
    counts = np.bincount(kmeans.labels_)

    dominant_color = colors[np.argmax(counts)]
    return dominant_color.astype(int)
