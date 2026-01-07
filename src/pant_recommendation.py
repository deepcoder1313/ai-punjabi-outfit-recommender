def recommend_pants(shirt_type, shirt_color):
    # Shirt type → pant type mapping
    pant_type_map = {
        "formal_shirt": ["jeans", "formal_trousers"],
        "casual_shirt": ["jeans", "chinos"],
        "t_shirt": ["jeans", "cargos"],
        "oversized_tshirt": ["cargos", "baggy_jeans"],
        "hoodie": ["joggers", "cargos"]
    }

    # Pant type → color mapping
    pant_color_map = {
        "formal_trousers": ["black", "grey", "navy"],
        "chinos": ["beige", "navy", "olive"],
        "jeans": ["blue", "black", "grey"],
        "cargos": ["olive", "khaki", "black"],
        "baggy_jeans": ["blue", "black"],
        "joggers": ["black", "grey"]
    }

    # Get pant types
    pant_types = pant_type_map.get(shirt_type, ["jeans"])

    # Collect colors
    pant_colors = set()
    for pant in pant_types:
        pant_colors.update(pant_color_map.get(pant, []))

    return pant_types, list(pant_colors)
