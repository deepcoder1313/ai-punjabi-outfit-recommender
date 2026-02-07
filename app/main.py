from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.routes.recommend import  router as recommend_router

# -------------------------
# CREATE FASTAPI APP
# -------------------------
app = FastAPI(title="AI Outfit Recommendation API")
from fastapi.staticfiles import StaticFiles

# Serve data folder as static files
app.mount("/static", StaticFiles(directory="data"), name="static")


# -------------------------
# CORS (for React frontend)
# -------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# INCLUDE ROUTES
# -------------------------
app.include_router(recommend_router)

# -------------------------
# STATIC FILE SERVING
# -------------------------
app.mount("/", StaticFiles(directory=".", html=False), name="static")

# -------------------------
# ROOT ROUTE
# -------------------------
@app.get("/")
def read_root():
    return {"message": "FastAPI server is running 🚀"}
