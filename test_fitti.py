
from src.fitti_recommendation import recommend_fitti

# Example case
shirt_fitti_color = "Cream"
primary_turban_color = "Maroon"

result = recommend_fitti(shirt_fitti_color, primary_turban_color)

print("Final FITTI Color:", result["fitti_color"])
print("Reason:", result["reason"])
