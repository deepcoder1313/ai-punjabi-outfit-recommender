from pant_recommendation import recommend_pants

shirt_type = "hoodie"
shirt_color = "black"

pant_types, pant_colors = recommend_pants(shirt_type, shirt_color)

print("👕 Shirt type:", shirt_type)
print("👖 Suggested pant types:", pant_types)
print("🎨 Suggested pant colors:", pant_colors)
