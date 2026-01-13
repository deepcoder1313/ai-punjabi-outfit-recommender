from fastapi import APIRouter, UploadFile, File
import shutil
import os

from app.core.model_loader import shirt_model
from src.predict_shirt_type import predict_shirt_type

router = APIRouter()

UPLOAD_DIR = "data/raw_images"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/predict-shirt-type")
async def predict_shirt_type_api(file: UploadFile = File(...)):
    """
    Accepts an image and predicts shirt type
    """

    image_path = os.path.join(UPLOAD_DIR, file.filename)

    # Save uploaded image
    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Predict using existing logic
    prediction = predict_shirt_type(image_path)

    return {
        "shirt_type": prediction
    }
