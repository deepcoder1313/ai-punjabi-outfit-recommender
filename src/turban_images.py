import os
import random


def get_primary_turban_images(color, base_path="data/turban_styles/primary", max_images=3):
    folder = os.path.join(base_path, color.lower().replace(" ", "_"))
    if not os.path.exists(folder):
        return []

    images = [
        os.path.join(folder, img)
        for img in os.listdir(folder)
        if img.lower().endswith((".jpg", ".jpeg", ".png"))
    ]

    return random.sample(images, min(len(images), max_images))


def get_fitti_images(fitti_color, base_path="data/turban_styles/fitti", max_images=2):
    folder = os.path.join(base_path, fitti_color.lower().replace(" ", "_"))
    if not os.path.exists(folder):
        return []

    images = [
        os.path.join(folder, img)
        for img in os.listdir(folder)
        if img.lower().endswith((".jpg", ".jpeg", ".png"))
    ]

    return random.sample(images, min(len(images), max_images))
