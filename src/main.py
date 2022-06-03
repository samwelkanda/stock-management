from typing import Dict, List, Union

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from .core.config import settings
from .database import get_db
from .models import Stock
from .schemas import CreateStock, UpdateStock

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)


@app.get("/")
def welcome() -> Dict:
    return {"msg": "Welcome to Stock Management API"}


@app.post("/stock", status_code=status.HTTP_201_CREATED)
def create_stock_entry(
    data: CreateStock, db: Session = Depends(get_db)) -> Union[Dict, Stock]:
    """Endpoint to create a stock entry

    Args:
        data (CreateStockRequest): Count of the stock
        db (Session, optional): Defaults to Depends(get_db).
        
    Returns:
        Stock: The created stock entry
    """
    if data.count < 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Failed. Stock count cannot be negative")
    new = Stock(count=data.count)
    db.add(new)
    db.commit()
    db.refresh(new)
    return new


@app.put("/stock/{stock_id}", status_code=status.HTTP_200_OK)
async def update_stock_entry(
    data: UpdateStock, db: Session = Depends(get_db)) -> Dict:
    """Endpoint to update a stock entry

    Args:
        data (UpdateStock): Count of the stock
        db (Session, optional): Defaults to Depends(get_db).
        
    Returns:
        Stock: The updated stock entry
    """
    if data.count < 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Failed. Stock count cannot be negative")
    if not db.query(Stock).filter(Stock.id == data.id).first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Stock with id {data.id} not found")
    # locks the row with the given id
    item = db.query(Stock).filter(Stock.id == data.id).with_for_update().one()
    item.count = data.count
    db.commit()  # saves and releases the lock
    return {"success": True, 'count': item.count}


@app.put("/stock/{stock_id}/purchase", status_code=status.HTTP_200_OK)
async def purchase_stock_(data: UpdateStock, db: Session = Depends(get_db)) -> Dict:
    """Endpoint to make a purchase against a stock

    Args:
        data (UpdateStock): Number of stock items to purchase
        db (Session, optional): Defaults to Depends(get_db).
        
    Returns:
        Stock: The remaining stock entry
    """
    if data.count < 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Failed. Stock count cannot be negative")
    if not db.query(Stock).filter(Stock.id == data.id).first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Stock with id {data.id} not found")
    # locks the row with the given id
    item = db.query(Stock).filter(Stock.id == data.id).with_for_update().one()
    if item.count >= data.count:
        item.count = item.count - data.count
        db.commit()  # saves and releases the lock
        return {"success": True, 'count': item.count}
    return {
        "success": False,
        'msg': "Not enough stock of {data.id} left for purchase."
    }
