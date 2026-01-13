import numpy as np


# Punjabi-friendly color palette for FITTI
FASHION_COLORS = {
    "White": [245, 245, 245],
    "Cream": [230, 220, 210],
    "Light Grey": [200, 200, 200],
    "Grey": [150, 150, 150],
    "Light Blue": [180, 200, 230],
    "Sky Blue": [160, 200, 220],
    "Beige": [220, 210, 190],
    "Off White": [235, 230, 225],
}


def rgb_distance(c1, c2):
    """Euclidean distance between two RGB colors"""
    return np.linalg.norm(np.array(c1) - np.array(c2))


def rgb_to_fitti_color(rgb):
    """
    Convert RGB value to closest FITTI color name
    """
    min_distance = float("inf")
    closest_color = None

    for color_name, color_rgb in FASHION_COLORS.items():
        dist = rgb_distance(rgb, color_rgb)
        if dist < min_distance:
            min_distance = dist
            closest_color = color_name

    return closest_color
