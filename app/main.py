from fastapi import FastAPI
from app.api.routes.predict import router as predict_router
from app.api.routes.recommend import router as recommend_router
from app.core.model_loader import shirt_model

app = FastAPI(title="AI Outfit Recommendation API")

app.include_router(predict_router)
app.include_router(recommend_router)

@app.get("/")
def read_root():
    return {"message": "FastAPI server is running 🚀"}
