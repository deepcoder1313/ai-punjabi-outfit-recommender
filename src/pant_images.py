import os
import random


def get_pant_images(pant_types, pant_colors, base_path="data/pant_styles", max_images=3):
    images = []

    for pant in pant_types:
        pant_folder = os.path.join(base_path, pant)

        if not os.path.exists(pant_folder):
            continue

        for color in pant_colors:
            color_folder = os.path.join(pant_folder, color)

            if os.path.exists(color_folder):
                files = [
                    os.path.join(color_folder, f)
                    for f in os.listdir(color_folder)
                    if f.lower().endswith((".jpg", ".jpeg", ".png"))
                ]

                images.extend(files)

    if images:
        return random.sample(images, min(len(images), max_images))

    return []
