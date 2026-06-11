from sqlalchemy.orm import Session
from fastapi import HTTPException

import requests
from app.models.order_model import Order



def check_inventory(product_id: int):

    response = requests.get(
        f"http://inventory-service:5600/inventory/{product_id}"

    )

    if response.status_code != 200:
        return None
    return response.json()


def create_order_service(
    order,
    db: Session
):
    
    inventory = check_inventory(
        order.product_id
    )

    if inventory is None:
        raise HTTPException(
            status_code=404,
            detail="Product inventory not found"
        )    

    if inventory["available_quantity"] < order.quantity:
        raise HTTPException(
            status_code=400,
            detail="Insufficient Stock"
        )
    

    reduce_inventory(
        order.product_id,
        order.quantity
    )

    new_order = Order(
        user_id=order.user_id,
        product_id=order.product_id,
        quantity=order.quantity,
        status="CREATED"

    )

    db.add(new_order)

    db.commit()
    
    db.refresh(new_order)

    return new_order


def get_all_orders_service(db: Session):
    return db.query(Order).all()


def get_order_by_id_service(
        order_id: int,
        db: Session
):

    existing_order = db.query(Order).filter(
        Order.id == order_id
    ).first()

    if existing_order is None:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )
    
    return existing_order


def update_order_service(
    order_id: int,
    order,
    db: Session
):
    
    existing_order = db.query(Order).filter(
        Order.id == order_id
    ).first()

    if existing_order is None:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )
    
    existing_order.status = order.status

    db.commit()

    db.refresh(existing_order)

    return existing_order


def delete_order_service(
        order_id: int,
        db: Session

):  
    existing_order = db.query(Order).filter(
        Order.id == order_id
    ).first()

    if existing_order is None:
        raise HTTPException(
            status_code=404,
            detail="Order Not found"
        )
    db.delete(existing_order)

    db.commit()

    return {
        "message": "Order deleted successfully"
    }


def reduce_inventory(
        product_id: int,
        quantity: int
):
    

    response = requests.put(
        f"http://inventory-service:5600/inventory/reduce/{product_id}",
        params={"quantity": quantity}
    )


    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.json()["detail"]
        )

    return response.json()

