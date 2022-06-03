from typing import List
from fastapi import FastAPI
from .core.config import settings

app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)

@app.get("/")
def welcome() -> dict:
    return {"msg":"Welcome to Stock Management API"}