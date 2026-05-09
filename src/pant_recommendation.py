import os
import random

import pant_images



def recommend_pants(shirt_type, shirt_colors):
    # 1️⃣ Pant type mapping
    pant_map = {
        "casual_shirt": ["jeans", "chinos"],
        "formal_shirt": ["formal_trousers", "chinos"],
        "t_shirt": ["jeans", "joggers"],
        "hoodie": ["joggers", "cargos"]
    }

    # 2️⃣ Pant color matching
    color_map = {
        "White": ["black", "navy", "grey", "olive"],
        "Black": ["grey", "blue", "beige"],
        "Navy Blue": ["grey", "black", "olive"],
        "Brown": ["beige", "black", "navy"],
        "Grey": ["black", "navy", "olive"]
    }

    pant_types = pant_map.get(shirt_type, ["jeans"])

    pant_colors = []
    for c in shirt_colors:
        pant_colors.extend(color_map.get(c, []))
    pant_colors = list(set(pant_colors))

    pant_images = {}
    base_dir = "data/pant_images"

    # 3️⃣ Collect images from color subfolders
    for pant in pant_types:
        pant_images[pant] = []
        pant_folder = os.path.join(base_dir, pant)

        if not os.path.exists(pant_folder):
            continue

        for color in pant_colors:
            color_folder = os.path.join(pant_folder, color)

            if not os.path.exists(color_folder):
                continue

            files = [
                f for f in os.listdir(color_folder)
                if f.lower().endswith((".jpg", ".jpeg", ".png"))
            ]

            for f in random.sample(files, min(2, len(files))):
                pant_images[pant].append(
    f"data/pant_images/{pant}/{color}/{f}"
)

    print(pant_images)  # move before return if needed
    return pant_types, pant_colors, pant_images
  