from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.inventory_schema import(
    InventoryCreate,
    InventoryUpdate,
    InventoryResponse
)

from app.services.inventory_service import (
    create_inventory_service,
    get_inventory_service,
    update_inventory_service,
    delete_inventory_service,
    reduce_inventory_service
)

router = APIRouter()


@router.post(
    "/inventory",
    response_model=InventoryResponse
)

def create_inventory(
    inventory: InventoryCreate,
    db: Session = Depends(get_db)

):    
    return create_inventory_service(
        inventory,
        db
    )



@router.get(
    "/inventory/{product_id}",
    response_model=InventoryResponse
)

def get_inventory(
    product_id: int,
    db: Session = Depends(get_db)
):
    return get_inventory_service(
        product_id,
        db
    )


@router.put(
    "/inventory/{product_id}",
    response_model=InventoryResponse 
)


def update_inventory(
    product_id: int,
    inventory: InventoryUpdate,
    db: Session = Depends(get_db)
):
    
    return update_inventory_service(
        product_id,
        inventory,
        db
    )
    


@router.delete(
    "/inventory/{product_id}"

)

def delete_inventory(
    product_id: int,
    db: Session = Depends(get_db)
):
    return delete_inventory_service(
        product_id,
        db
    )
    
@router.put("/inventory/reduce/{product_id}")

def reduce_inventory(
    product_id: int,
    quantity: int,
    db: Session = Depends(get_db)
):
    return reduce_inventory_service(
        product_id,
        quantity,
        db
    )
