from pydantic import BaseModel

class CreateStock(BaseModel):
    count: int

class GetStock(BaseModel):
    id: int
    count: int
    