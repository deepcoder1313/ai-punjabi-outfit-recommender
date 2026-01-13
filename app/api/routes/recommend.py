from fastapi import APIRouter, UploadFile, File
import os
import shutil
import colorsys
import numpy as np

from src.predict_shirt_type import predict_shirt_type
from src.color_extraction import extract_dominant_color
from src.color_matching import match_colors
from src.pant_recommendation import recommend_pants
from src.turban_recommendation import recommend_turban

router = APIRouter()

UPLOAD_DIR = "data/raw_images"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/recommend-outfit")
async def recommend_outfit(file: UploadFile = File(...)):
    """
    Complete Outfit Recommendation API
    """

    try:
        # ------------------------------------------------
        # 1️⃣ Save uploaded image
        # ------------------------------------------------
        image_path = os.path.join(UPLOAD_DIR, file.filename)

        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # ------------------------------------------------
        # 2️⃣ Predict shirt type (ML)
        # ------------------------------------------------
        shirt_type = predict_shirt_type(image_path)
        shirt_type = str(shirt_type)  # ensure pure Python string

        # ------------------------------------------------
        # 3️⃣ Extract dominant color (SAFE)
        # ------------------------------------------------
        dominant_rgb = extract_dominant_color(image_path)

        # FORCE flatten + convert NumPy → Python floats
        dominant_rgb = np.array(dominant_rgb).reshape(-1)

        if dominant_rgb.shape[0] < 3:
            raise ValueError(f"Invalid dominant_rgb shape: {dominant_rgb}")

        r = float(dominant_rgb[0])
        g = float(dominant_rgb[1])
        b = float(dominant_rgb[2])

        # ------------------------------------------------
        # 4️⃣ Convert RGB → HSV (NO OpenCV)
        # ------------------------------------------------
        r, g, b = r / 255.0, g / 255.0, b / 255.0
        h, s, v = colorsys.rgb_to_hsv(r, g, b)

        hsv = [
            int(h * 179),
            int(s * 255),
            int(v * 255)
        ]  # pure Python list

        # ------------------------------------------------
        # 5️⃣ Match shirt colors
        # ------------------------------------------------
        shirt_colors = match_colors(hsv)
        shirt_colors = [str(c) for c in list(shirt_colors)]

        # ------------------------------------------------
        # 6️⃣ Recommend pants
        # ------------------------------------------------
        pant_types, pant_colors = recommend_pants(
            shirt_type,
            shirt_colors
        )

        pant_types = [str(p) for p in pant_types]
        pant_colors = [str(c) for c in pant_colors]

        # ------------------------------------------------
        # 7️⃣ Recommend turban + FITTI
        # ------------------------------------------------
        turban_result = recommend_turban(shirt_colors, shirt_type)
        

        turban_colors = [
            str(c) for c in turban_result.get("turban_colors", [])
        ]

        fitti_color = turban_result.get("fitti_color")
        if fitti_color is not None:
            fitti_color = str(fitti_color)

        # ------------------------------------------------
        # 8️⃣ Final response
        # ------------------------------------------------
        return {
            "shirt": {
                "type": shirt_type,
                "matching_colors": shirt_colors
            },
            "pants": {
                "types": pant_types,
                "colors": pant_colors
            },
            "turban": {
                "primary_colors": turban_colors,
                "fitti_color": fitti_color
            }
        }

    except Exception as e:
        import traceback
        return {
            "error": str(e),
            "trace": traceback.format_exc()
        }
