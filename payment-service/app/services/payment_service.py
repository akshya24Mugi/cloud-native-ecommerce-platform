from sqlalchemy.orm import Session

from fastapi import HTTPException

from app.models.payment_model import Payment


def create_payment_service(
        payment,
        db: Session
):
    new_payment = Payment(
        order_id=payment.order_id,
        amount=payment.amount,
        payment_status="SUCCESS"
    )

    db.add(new_payment)

    db.commit()

    db.refresh(new_payment)

    return new_payment



def get_all_payments_service(db: Session):
    return db.query(Payment).all()



def get_payment_by_id_service(
        payment_id: int,
        db: Session
):
    
    existing_payment = db.query(Payment).filter(
        Payment.id == payment_id
    ).first()

    if existing_payment is None:
        
        raise HTTPException(
            status_code=404,
            detail="Payment not found"
        )
    
    return existing_payment



def update_payment_service(
        payment_id: int,
        payment,
        db: Session
):
    
    existing_payment = db.query(Payment).filter(
        Payment.id == payment_id
    ).first()

    if existing_payment is None:
        
        raise HTTPException(
            status_code=404,
            detail="Payment not found"
        )
    
    existing_payment.payment_status = payment.payment_status

    db.commit()

    db.refresh(existing_payment)

    return existing_payment


def delete_payment_service(
        payment_id: int,
        db: Session
):
    existing_payment = db.query(Payment).filter(
        Payment.id == payment_id
    
    ).first()


    if existing_payment is None:
        raise HTTPException(
            status_code=404,
            detail="Payment not found"
        )
    
    db.delete(existing_payment)

    db.commit()

    return {
        "message": "Payment deleted successfully"
    }