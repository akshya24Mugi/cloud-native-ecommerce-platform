from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.inventory_model import Inventory


def create_inventory_service(
        inventory,
        db: Session
):
    
    new_inventory = Inventory(
        product_id=inventory.product_id,
        available_quantity=inventory.available_quantity
    )

    db.add(new_inventory)

    db.commit()

    db.refresh(new_inventory)

    return new_inventory



def get_inventory_service(
        product_id: int,
        db: Session
):
    
    inventory = db.query(Inventory).filter(
        Inventory.product_id == product_id
    ).first()

    if inventory is None:
        raise HTTPException(
            status_code=404,
            detail="Inventory not found"
        )
    
    return inventory


def update_inventory_service(
        product_id: int,
        inventory,
        db: Session
):
    
    existing_inventory = db.query(Inventory).filter(
        Inventory.product_id == product_id

    ).first()

    if existing_inventory is None:
        raise HTTPException(
            status_code=404,
            details="Inventory not found"
        )

    existing_inventory.available_quantity = (
        inventory.available_quantity
    )

    db.commit()

    db.refresh(existing_inventory)

    return existing_inventory



def delete_inventory_service(
        product_id: int,
        db: Session
):
    
    existing_inventory = db.query(Inventory).filter(
        Inventory.product_id == product_id
    
    ).first()
    

    if existing_inventory is None:
        raise HTTPException(
            status_code=404,
            detail="Inventory not found"
        )
    
    db.delete(existing_inventory)

    db.commit()

    return {
        "message": "Inventory deleted successfully"
    }



def reduce_inventory_service(
    product_id: int,
    quantity: int,
    db: Session
):

    inventory = db.query(Inventory).filter(
        Inventory.product_id == product_id
    ).first()


    if inventory is None:
        raise HTTPException(
            status_code=404,
            detail="Inventory not found"
        )
    
    if inventory.available_quantity < quantity:
        
        raise HTTPException(
            status_code=400,
            detail="Insufficient Stock"
        )

    inventory.available_quantity -= quantity

    db.commit()
    
    db.refresh(inventory)

    return inventory