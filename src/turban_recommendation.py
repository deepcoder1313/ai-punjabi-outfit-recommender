def recommend_turban(shirt_color_category, shirt_type):
    """
    Recommend turban (pagri) colors based on Punjabi cultural styling rules.

    Parameters:
    - shirt_color_category (str): light, dark, pastel, white
    - shirt_type (str): formal_shirt, casual_shirt, t_shirt, hoodie

    Returns:
    - dict with recommended colors and explanation
    """

    recommendations = []
    reasons = []

    # ---------- RULE 1: White / Light Shirts ----------
    if shirt_color_category in ["white", "light"]:
        recommendations = ["Navy Blue", "Maroon", "Black", "Mustard"]
        reasons.append(
            "Light or white shirts allow high-contrast turbans, which is a common Punjabi styling choice."
        )

    # ---------- RULE 2: Dark Shirts ----------
    elif shirt_color_category == "dark":
        recommendations = ["White", "Cream", "Light Grey", "Pastel Blue"]
        reasons.append(
            "Dark shirts are best balanced with lighter turban colors to maintain visual harmony."
        )

    # ---------- RULE 3: Pastel Shirts ----------
    elif shirt_color_category == "pastel":
        recommendations = ["Wine", "Royal Blue", "Olive", "Bottle Green"]
        reasons.append(
            "Pastel shirts pair well with rich and deep turban shades for an elegant Punjabi look."
        )

    # ---------- SHIRT TYPE ADJUSTMENTS ----------
    if shirt_type == "formal_shirt":
        recommendations = [
            color for color in recommendations
            if color in ["Navy Blue", "Black", "Wine", "Dark Grey", "Maroon"]
        ]
        reasons.append(
            "Formal shirts traditionally pair best with solid and sober turban colors."
        )

    elif shirt_type in ["casual_shirt", "t_shirt", "hoodie"]:
        recommendations = recommendations + ["Kesari", "Olive"]
        reasons.append(
            "Casual and youth outfits allow more vibrant and trendy turban colors."
        )

    # Remove duplicates while preserving order
    recommendations = list(dict.fromkeys(recommendations))

    return {
        "turban_colors": recommendations,
        "explanation": reasons
    }
