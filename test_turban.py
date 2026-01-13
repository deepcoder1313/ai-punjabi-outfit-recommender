from src.turban_recommendation import recommend_turban

# Example test
result = recommend_turban(
    shirt_color_category="white",
    shirt_type="casual_shirt"
)

print("Recommended Turban Colors:")
for color in result["turban_colors"]:
    print("-", color)

print("\nExplanation:")
for reason in result["explanation"]:
    print("-", reason)
