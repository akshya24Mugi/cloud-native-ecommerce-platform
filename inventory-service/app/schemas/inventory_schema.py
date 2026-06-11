from pydantic import BaseModel

class InventoryCreate(BaseModel):


    product_id: int
    available_quantity: int


class InventoryUpdate(BaseModel):
        available_quantity: int


class InventoryResponse(BaseModel):
      
    id: int
    product_id: int
    available_quantity: int

    class Config:

         from_attributes = True    