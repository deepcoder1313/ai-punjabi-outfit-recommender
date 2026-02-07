import cv2
import numpy as np
import os
from sklearn.cluster import KMeans
from src.shirt_area_detection import extract_shirt_region
from src.shirt_area_detection import extract_shirt_region


def extract_dominant_color(image_path, k=3):
    image_path = os.path.abspath(image_path)

    shirt_region = extract_shirt_region(image_path)

    if shirt_region is None:
        img = extract_shirt_region(image_path)

        if image is None:
            raise ValueError(f"Image not found or path is wrong: {image_path}")
    else:
        image = shirt_region

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pixels = image_rgb.reshape((-1, 3))

    kmeans = KMeans(n_clusters=k, n_init=10)
    kmeans.fit(pixels)

    colors = kmeans.cluster_centers_
    counts = np.bincount(kmeans.labels_)

    sorted_indices = np.argsort(-counts)

    dominant_color = colors[sorted_indices[0]]
    secondary_color = colors[sorted_indices[1]] if len(sorted_indices) > 1 else dominant_color

    # 🚨 MUST RETURN EXACTLY 2 VALUES
    return dominant_color.astype(int), secondary_color.astype(int)
