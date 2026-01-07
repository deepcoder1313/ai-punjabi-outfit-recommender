# ==============================
# STEP 0: Import all components
# ==============================

from color_extraction import extract_dominant_color
from color_matching import match_colors
from predict_shirt_type import predict_shirt_type
from pant_recommendation import recommend_pants


# ==============================
# STEP 1: Input image
# ==============================

image_path = r"C:\Users\Sandeep\Documents\outfit_color_ai\data\raw_images\shirt.jpg"


# ==============================
# STEP 2: Color extraction
# ==============================

dominant_rgb = extract_dominant_color(image_path)
print("🎨 Dominant RGB:", dominant_rgb)


# ==============================
# STEP 3: Color matching
# ==============================

shirt_color_suggestions = match_colors(dominant_rgb)
print("🎨 Shirt-based matching colors:", shirt_color_suggestions)


# ==============================
# STEP 4: Shirt type prediction (DL)
# ==============================

shirt_type = predict_shirt_type(image_path)
print("👕 Predicted shirt type:", shirt_type)


# ==============================
# STEP 5: Pant recommendation (Logic)
# ==============================

pant_types, pant_colors = recommend_pants(shirt_type, shirt_color_suggestions)


# ==============================
# STEP 6: Final result
# ==============================

print("\n✅ FINAL OUTFIT RECOMMENDATION")
print("👕 Shirt type:", shirt_type)
print("🎨 Shirt color suggestions:", shirt_color_suggestions)
print("👖 Recommended pant types:", pant_types)
print("🎨 Recommended pant colors:", pant_colors)
