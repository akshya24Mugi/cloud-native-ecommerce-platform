from sqlalchemy.orm import Session

from app.models.product_model import Product

from fastapi import HTTPException


def create_product_service(
        
    product,
    db: Session
):
    
    new_product = Product(
        name=product.name,
        description=product.description,
        price=product.price,
        category=product.category
    )

    db.add(new_product)

    db.commit()

    db.refresh(new_product)

    return new_product


def get_all_products_service(db: Session):

    return db.query(Product).all()


def get_product_by_id_service(
        product_id: int,
        db: Session
):
    
    product = db.query(Product).filter(
        Product.id == product_id
    ).first()   

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product Not found"
        )
    return product



def update_product_service(
        product_id: int,
        product,
        db: Session
):
    
    existing_product = db.query(Product).filter(
        Product.id == product_id

    ).first()

    if existing_product is None:

        raise HTTPException(
            status_code=404,
            details="Product Not Found"
        )
    
    existing_product.name = product.name
    existing_product.description = product.description
    existing_product.price = product.price
    existing_product.category = product.category

    db.commit()

    db.refresh(existing_product)

    return existing_product


def delete_product_service(
    product_id: int,
    db: Session
):
    
    existing_product = db.query(Product).filter(
        product_id == product_id
    ).first()

    if existing_product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    
    db.delete(existing_product)

    db.commit()

    return {
        "message": "Product deleted successfully"
    }