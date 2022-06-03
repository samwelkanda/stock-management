from sqlalchemy import Integer
from sqlalchemy.sql.schema import Column
from .database import Base

class Stock(Base):    
    __tablename__ = 'stock'
    
    id = Column(Integer, primary_key=True)
    count = Column(Integer)