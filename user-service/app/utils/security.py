import bcrypt
from jose import jwt
from datetime import datetime, timedelta, timezone
from jose import JWTError

from app.config import settings

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.JWT_ALGORITHM


def hash_password(password: str):
    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()

    )
    return hashed_password.decode("utf-8")


def verify_password(password: str, hashed_password: str):

    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )

def create_access_token(data: dict):

    payload = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=30)

    payload.update({"exp": expire}) 

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM

    )    

    return token

def verify_access_token(token: str):
    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except JWTError:

        return None
