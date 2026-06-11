from sqlalchemy.orm import Session
from app.models.user_model import User

from app.utils.security import (
    hash_password,
    verify_password,
    create_access_token
)

from fastapi import HTTPException

def register_user_service(user, db: Session):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered."
        )
    
    new_user =  User(
        username=user.username,
        email=user.email,
        password_hash=hash_password(user.password)


    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "user_id": new_user.id,
        "username": new_user.username,
        "email": new_user.email
    }

def login_user_service(user, db: Session):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    
    if existing_user is None:
        
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if not verify_password(
        user.password,
        existing_user.password_hash
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    access_token = create_access_token(
        {
            "sub": existing_user.email
        }
    )

    return {
        "message": "Login successful",
        "access_token": access_token
    }

def get_profile_service(payload, db: Session):
    
    email = payload.get("sub")

    user = db.query(User).filter(
        User.email == email

    ).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    


    return {
        "id": user.id,
        "username": user.username,
        "email": user.email
    }
