from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.responses import Response
from app.api.routes.recommend import router as recommend_router

app = FastAPI(title="AI Outfit Recommendation API")
class CustomStaticFiles(StaticFiles):
    async def get_response(self, path, scope):
        response = await super().get_response(path, scope)

        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "*"
        response.headers["Cache-Control"] = "public, max-age=31536000"

        return response
# Static (optional)
app.mount("/static", CustomStaticFiles(directory="data"), name="static")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://aiclothpunjabi.netlify.app",
    ],
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