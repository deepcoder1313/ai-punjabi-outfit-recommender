from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.routes.recommend import router as recommend_router

app = FastAPI(title="AI Outfit Recommendation API")

# Static (optional)
app.mount("/static", StaticFiles(directory="data"), name="static")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(recommend_router)

# Root
@app.get("/")
def read_root():
    return {"message": "FastAPI server is running 🚀"}