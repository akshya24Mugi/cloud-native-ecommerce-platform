from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.payment_schemas import(
    PaymentCreate,
    PaymentUpdate,
    PaymentResponse
)

from app.services.payment_service import(
    create_payment_service,
    get_all_payments_service,
    get_payment_by_id_service,
    update_payment_service,
    delete_payment_service
)

router = APIRouter()

@router.post(
    "/payments",
    response_model=PaymentResponse
)

def create_payment(
    payment: PaymentCreate,
    db: Session = Depends(get_db)
):
    
    return create_payment_service(
        payment,
        db
    )

@router.get(
    "/payments",
    response_model=list[PaymentResponse]
)

def get_all_payments(
    db: Session = Depends(get_db)

):
    
    return get_all_payments_service(db)


@router.get(
    "/payments/{payment_id}",
    response_model=PaymentResponse
)

def get_payment_by_id(
    payment_id: int,
    db: Session = Depends(get_db)
):
    
    return get_payment_by_id_service(
        payment_id,
        db
    )



@router.put(
    "/payments/{payment_id}",
    response_model=PaymentResponse
)

def update_payment(
    payment_id: int,
    payment: PaymentUpdate,
    db: Session = Depends(get_db)
):
    
    return update_payment_service(
        payment_id,
        payment,
        db
    )


@router.delete(
    "/payments/{payment_id}"
)

def delete_payment(
    payment_id: int,
    db: Session = Depends(get_db)
):
    return delete_payment_service(
        payment_id,
        db
    )