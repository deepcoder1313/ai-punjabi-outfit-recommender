import os
import random

def recommend_celebrity_outfits(pant_types, pant_colors):
    base_dir = "data/celebrity_outfits"
    results = []

    for pant in pant_types:
        for color in pant_colors:
            path = os.path.join(base_dir, pant, color)
            if os.path.exists(path):
                images = os.listdir(path)
                if images:
                    chosen = random.choice(images)
                    results.append(os.path.join(path, chosen))

    return results
