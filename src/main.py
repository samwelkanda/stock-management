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

@app.post("/stock", status_code = status.HTTP_201_CREATED)
def create_stock_entry(data: CreateStock, db: Session = Depends(get_db)) -> Union[Dict, Stock]:
    """Endpoint to create a stock entry

    Args:
        data (CreateStockRequest): Count of the stock
        db (Session, optional): Defaults to Depends(get_db).
        
    Returns:
        Stock: The created stock entry
    """
    if data.count < 0:
        return {
        "success": False,
        "error": "Failed. Stock count cannot be negative"
    }
        
    new = Stock(count = data.count)
    db.add(new)
    db.commit()
    db.refresh(new)
    return new