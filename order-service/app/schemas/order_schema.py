from pydantic import BaseModel

class OrderCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int


class OrderUpdate(BaseModel):

    status: str

class OrderResponse(BaseModel):

    id: int
    user_id: int
    product_id: int
    quantity: int
    status: str

    class Config:

        from_attributes = True