import cv2


def extract_shirt_region(image_path):
    img = cv2.imread(image_path)

    if img is None:
        raise ValueError("Image not found or path is wrong")

    h, w, _ = img.shape

    # Shirt area (heuristic crop)
    y1 = int(0.20 * h)
    y2 = int(0.75 * h)

    x1 = int(0.15 * w)
    x2 = int(0.85 * w)

    cropped = img[y1:y2, x1:x2]

    return cropped
