import os
from predict_shirt_type import predict_shirt_type

IMAGE_DIR = r"C:\Users\Sandeep\Documents\outfit_color_ai\data\raw_images"

for file in os.listdir(IMAGE_DIR):
    if file.lower().endswith((".jpg", ".png", ".jpeg")):
        image_path = os.path.join(IMAGE_DIR, file)
        shirt_type = predict_shirt_type(image_path)
        print(f"{file} → 👕 {shirt_type}")
