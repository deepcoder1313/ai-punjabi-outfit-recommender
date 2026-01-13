from src.color_extraction import extract_top_colors
from src.fitti_color_mapping import rgb_to_fitti_color

image_path = "data/raw_images/shirt1.jpg"
dominant, secondary = extract_top_colors(image_path)

fitti_color = rgb_to_fitti_color(secondary)

print("Dominant RGB:", dominant)
print("Secondary RGB:", secondary)
print("Fitti Color (from shirt):", fitti_color)

