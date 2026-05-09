from fastapi import APIRouter, UploadFile, File, Request
import os
import shutil
import uuid

from src.color_extraction import extract_dominant_color
from src.color_matching import match_colors
from src.predict_shirt_type import predict_shirt_type
from src.pant_recommendation import recommend_pants
from src.turban_recommendation import recommend_turban_and_fitti

router = APIRouter(prefix="/recommend-outfit")


@router.post("/")
async def recommend_outfit(
    request: Request,
    file: UploadFile = File(...)
):

    try:
        # -------------------------------
        # save uploaded image
        # -------------------------------
        upload_dir = "data/raw_images"
        os.makedirs(upload_dir, exist_ok=True)

        filename = f"{uuid.uuid4()}_{file.filename}"
        image_path = os.path.join(upload_dir, filename)

        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # -------------------------------
        # base url + helper
        # -------------------------------
        BASE_URL = "https://ai-punjabi-outfit-recommender-4.onrender.com"

        def to_url(path: str):
            path = path.replace("\\", "/")

            # already a url → return directly
            if path.startswith("http") :
                return path

            # remove absolute part if accidentally passed
            if "data/" in path:
                rel = path.split("data/", 1)[1]
            else:
                # fallback (do not crash)
                rel = path.lstrip("/")

            return f"{BASE_URL}/static/{rel}"

        # -------------------------------
        # color extraction
        # -------------------------------
        dominant_rgb, secondary_rgb = extract_dominant_color(image_path)

        # -------------------------------
        # shirt color names
        # -------------------------------
        shirt_colors = match_colors(dominant_rgb)

        # -------------------------------
        # shirt type
        # -------------------------------
        shirt_type = predict_shirt_type(image_path)

        # -------------------------------
        # pant recommendation
        # -------------------------------
        pant_types, pant_colors, pant_images_raw = recommend_pants(
            shirt_type,
            shirt_colors
        )

        # -------------------------------
        # convert pant images to urls
        # -------------------------------
        pant_images = {}

        for ptype, img_list in pant_images_raw.items():
            pant_images[ptype] = [to_url(img) for img in img_list]

        # -------------------------------
        # turban + fitti
        # -------------------------------
        turban_result = recommend_turban_and_fitti(
            secondary_rgb=secondary_rgb
        )

        # -------------------------------
        # convert turban images to urls
        # -------------------------------
        turban_images = {}

        for color, img_list in turban_result["turban_images"].items():
            turban_images[color] = [to_url(img) for img in img_list]

        # -------------------------------
        # convert fitti images to urls
        # -------------------------------
        fitti_images = [to_url(img) for img in turban_result["fitti_images"]]

        # -------------------------------
        # response
        # -------------------------------
        return {
            "shirt_type": shirt_type,
            "shirt_colors": shirt_colors,

            "pant_types": pant_types,
            "pant_colors": pant_colors,
            "pant_images": pant_images,

            "turban_primary": turban_result["turban_primary"],
            "turban_images": turban_images,

            "fitti_color": turban_result["fitti_color"],
            "fitti_images": fitti_images,
        }

    except Exception as e:
        return {
            "error": str(e)
        }
 