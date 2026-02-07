import os
from src.shirt_area_detection import extract_shirt_region
import cv2


def predict_shirt_type(image_path: str) -> str:
    """
    TEMPORARY fallback logic until ML is stable.
    Uses filename keywords as heuristic.
    """
    img = extract_shirt_region(image_path)

    name = os.path.basename(image_path).lower()

    if "hoodie" in name:
        return "hoodie"
    elif "tshirt" in name or "t-shirt" in name:
        return "tshirt"
    elif "formal" in name or "shirt" in name:
        return "formal_shirt"
    else:
        return "casual_shirt"
