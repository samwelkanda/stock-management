from pydantic import BaseModel


class CreateStock(BaseModel):
    count: int


class UpdateStock(BaseModel):
    id: int
    count: int
