from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.order_schema import (
    OrderCreate,
    OrderUpdate,
    OrderResponse
)

from app.services.order_service import (
    create_order_service,
    get_all_orders_service,
    get_order_by_id_service,
    update_order_service,
    delete_order_service
)

router = APIRouter()


@router.post(
    "/orders",
    response_model=OrderResponse
)
def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db)
):
    
    return create_order_service(
        order,
        db
    )


@router.get(
    "/orders",
    response_model=list[OrderResponse]
)
def get_all_orders(
    db: Session = Depends(get_db)
):
    
    return get_all_orders_service(db)




@router.get(
    "/orders/{order_id}",
    response_model=OrderResponse    
)

def get_order_by_id(
    order_id: int,
    db: Session = Depends(get_db)

):
    return get_order_by_id_service(
        order_id,
        db
    )



@router.put(
    "/orders/{order_id}",
    response_model=OrderResponse
)

def update_order(
    order_id: int,
    order: OrderUpdate,
    db: Session = Depends(get_db)
):
    
    return update_order_service(
        order_id,
        order,
        db

    )    


@router.delete(
    "/orders/{order_id}"
)
def delete_order(
    order_id: int,
    db: Session = Depends(get_db)
):

    return delete_order_service(
        order_id,
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

