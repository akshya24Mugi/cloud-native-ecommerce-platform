from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.product_schema import (
    ProductCreate,
    ProductUpdate,
    ProductResponse
)

from app.services.product_service import (
    create_product_service,
    get_all_products_service,
    get_product_by_id_service,
    update_product_service,
    delete_product_service
)

router = APIRouter()

@router.post(
    "/products",
    response_model=ProductResponse
)


def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    
    return create_product_service(
        product,
        db
    )


@router.get(
    "/products",
    response_model=list[ProductResponse]

)
def get_all_products(
    db: Session = Depends(get_db)

):
    return get_all_products_service(db)


@router.get(
    "/products/{product_id}",
    response_model=ProductResponse

)

def get_product_by_id(
    product_id: int,
    db: Session = Depends(get_db)
):
    return get_product_by_id_service(
        product_id,
        db
    )


@router.put(
    "/products/{product_id}",
    response_model=ProductResponse
)

def update_product(
    product_id: int,
    product: ProductUpdate,
    db: Session = Depends(get_db)
):
    
    return update_product_service(
        product_id,
        product,
        db
    )
    

@router.delete(
    "/products/{product_id}"
)

def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    
    return delete_product_service(
        product_id,
        db 
    )
    
