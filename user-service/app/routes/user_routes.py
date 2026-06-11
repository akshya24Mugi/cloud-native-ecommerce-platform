from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user_schema import UserRegister
from app.services.user_service import register_user_service
from app.database.database import get_db
from app.utils.auth import get_current_user
from app.services.user_service import get_profile_service


from app.schemas.user_schema import (
    UserRegister,
    UserLogin
)

from app.services.user_service import (
    register_user_service,
    login_user_service
)

router = APIRouter()

@router.post("/users/register")
def register_user(
    user: UserRegister,
    db: Session = Depends(get_db)

):
    
    return register_user_service(user, db)

@router.post("/users/login")
def login_users(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    
    return login_user_service(user, db)


@router.get("/users/profile")
def get_profile(
    payload = Depends(get_current_user),
    db : Session = Depends(get_db)

):
    return get_profile_service(
        payload,
        db
    )









