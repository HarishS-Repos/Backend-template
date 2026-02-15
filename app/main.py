from fastapi import FastAPI
from app.api.v1.routes import router
from app.core.logging import setup_logging

setup_logging()

app = FastAPI(
    title="AI Backend Spine",
    version="1.0.0"
)

app.include_router(router, prefix="/api/v1")
