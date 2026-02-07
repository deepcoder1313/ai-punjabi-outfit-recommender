import os
import math
import colorsys

# -----------------------------------------
# Reference colors for your folder names
# -----------------------------------------

COLOR_RGB = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "off_white": (245, 245, 235),
    "cream": (245, 245, 220),
    "light_grey": (210, 210, 210),
    "grey": (150, 150, 150),

    "maroon": (128, 0, 32),
    "rust maroon": (150, 60, 60),
    "maroon wine": (120, 30, 40),

    "navy_blue": (0, 0, 128),
    "navy blue": (0, 0, 128),
    "royal blue": (65, 105, 225),

    "ferozi": (64, 224, 208),
    "light ferozi": (150, 230, 220),

    "olive wood": (110, 110, 60),
    "pista": (152, 251, 152),

    "khaki dark": (107, 94, 38),
    "light coffee": (181, 101, 29),

    "pink peach": (255, 200, 200),
    "gajri pink": (255, 105, 180),
    "pyaji pink": (215, 40, 80),

    "peach rust": (205, 92, 92),
    "orange mustard": (204, 153, 0),

    "mauve": (176, 146, 179),
    "dark mauve fitti": (140, 110, 150),

    "mouse grey fitti": (160, 160, 160),
    "greenish grey fitti": (170, 180, 170),
    "light military fitti": (120, 130, 90),
}


# -----------------------------------------
# helpers
# -----------------------------------------

def normalize_name(name: str):
    name = name.lower()
    name = name.replace("_", " ")
    name = name.replace("-", " ")
    return name.strip()


def rgb_to_hsv01(rgb):
    r, g, b = rgb
    return colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)


def hsv_distance(a, b):
    return math.sqrt(
        (a[0] - b[0]) ** 2 +
        (a[1] - b[1]) ** 2 +
        (a[2] - b[2]) ** 2
    )


# -----------------------------------------
# Main function
# -----------------------------------------

def recommend_turban_and_fitti(
    secondary_rgb,
    turban_base_dir="data/turban_images",
    fitti_base_dir="data/fitti_images",
    top_k=3
):
    """
    secondary_rgb : (r,g,b)
    """

    shirt_hsv = rgb_to_hsv01(secondary_rgb)

    # ------------------------------------------------
    # TURBAN RANKING
    # ------------------------------------------------

    turban_scores = []

    if os.path.isdir(turban_base_dir):

        for folder in os.listdir(turban_base_dir):
            folder_path = os.path.join(turban_base_dir, folder)

            if not os.path.isdir(folder_path):
                continue

            key = normalize_name(folder)

            if key not in COLOR_RGB:
                continue

            turban_rgb = COLOR_RGB[key]
            turban_hsv = rgb_to_hsv01(turban_rgb)

            dist = hsv_distance(shirt_hsv, turban_hsv)

            turban_scores.append((dist, folder))

    turban_scores.sort(key=lambda x: x[0])

    selected_turbans = [x[1] for x in turban_scores[:top_k]]

    turban_images = {}

    for name in selected_turbans:
        path = os.path.join(turban_base_dir, name)

        images = []
        for f in os.listdir(path):
            if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
                images.append(os.path.join(path, f))

        turban_images[name] = images


    # ------------------------------------------------
    # FITTI RANKING
    # ------------------------------------------------

    fitti_scores = []

    if os.path.isdir(fitti_base_dir):

        for folder in os.listdir(fitti_base_dir):
            folder_path = os.path.join(fitti_base_dir, folder)

            if not os.path.isdir(folder_path):
                continue

            key = normalize_name(folder)

            if key not in COLOR_RGB:
                continue

            fitti_rgb = COLOR_RGB[key]
            fitti_hsv = rgb_to_hsv01(fitti_rgb)

            dist = hsv_distance(shirt_hsv, fitti_hsv)

            fitti_scores.append((dist, folder))

    fitti_scores.sort(key=lambda x: x[0])

    best_fitti = fitti_scores[0][1] if fitti_scores else None

    fitti_images = []

    if best_fitti:
        fitti_path = os.path.join(fitti_base_dir, best_fitti)

        for f in os.listdir(fitti_path):
            if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
                fitti_images.append(os.path.join(fitti_path, f))


    return {
        "turban_primary": selected_turbans,
        "turban_images": turban_images,
        "fitti_color": best_fitti,
        "fitti_images": fitti_images
    }
