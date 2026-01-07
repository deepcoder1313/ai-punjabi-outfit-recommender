from color_extraction import extract_dominant_color
from color_matching import rgb_to_hsv, match_colors
from predict_shirt_type import predict_shirt_type

image_path = r"C:\Users\Sandeep\Documents\outfit_color_ai\data\raw_images\images.jpg"

rgb_color = extract_dominant_color(image_path)
print("RGB:", rgb_color)

hsv_color = rgb_to_hsv(rgb_color)
print("HSV:", hsv_color)

suggestions = match_colors(hsv_color)
print("Suggested outfit colors:", suggestions)

shirt_type = predict_shirt_type(image_path)
print("Predicted shirt type:", shirt_type)
