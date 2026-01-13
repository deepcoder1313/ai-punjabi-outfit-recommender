import cv2
import numpy as np
from sklearn.cluster import KMeans


def extract_dominant_color(image_path, k=4):
    """
    Extract dominant and secondary colors from an image.

    Returns:
    - dominant_rgb: most frequent color
    - secondary_rgb: second most frequent color
    """

    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Image not found or invalid path")

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img.reshape((-1, 3))

    kmeans = KMeans(n_clusters=k, n_init=10)
    labels = kmeans.fit_predict(img)

    counts = np.bincount(labels)
    centers = kmeans.cluster_centers_

    # Sort clusters by frequency (descending)
    sorted_indices = np.argsort(counts)[::-1]

    dominant_rgb = centers[sorted_indices[0]].astype(int)
    secondary_rgb = centers[sorted_indices[1]].astype(int)

    return dominant_rgb, secondary_rgb

