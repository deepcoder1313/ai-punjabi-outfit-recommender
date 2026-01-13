def recommend_fitti(
    shirt_fitti_color,
    primary_turban_color
):
    """
    Final FITTI selection logic based on Punjabi styling rules.

    Rules:
    - FITTI comes from shirt's least dominant color
    - FITTI must be different from primary turban color
    """

    # Normalize inputs
    shirt_fitti_color = shirt_fitti_color.lower()
    primary_turban_color = primary_turban_color.lower()

    # Fallback neutral colors
    fallback_colors = ["cream", "off white", "light grey", "beige"]

    # Rule 1: Ideal case
    if shirt_fitti_color != primary_turban_color:
        return {
            "fitti_color": shirt_fitti_color.title(),
            "reason": (
                f"{shirt_fitti_color.title()} is the least dominant shirt color "
                "and balances the turban near the face."
            )
        }

    # Rule 2: Conflict case → choose fallback
    for color in fallback_colors:
        if color != primary_turban_color:
            return {
                "fitti_color": color.title(),
                "reason": (
                    f"Shirt secondary color matched the turban color, "
                    f"so {color.title()} is used to maintain visual balance."
                )
            }

    # Absolute fallback (rare)
    return {
        "fitti_color": "Cream",
        "reason": "Neutral fallback used for balanced Punjabi fitti."
    }
