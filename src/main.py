from typing import Dict, List, Union
from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session

from .core.config import settings
from .database import get_db
from .models import Stock
from .schemas import CreateStock, GetStock


app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)

@app.get("/")
def welcome() -> Dict:
    return {"msg":"Welcome to Stock Management API"}