from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from app.domain.models import User
from app.infrastructure.database import SessionLocal
from app.domain.exceptions import UserNotFoundError

# JWT ayarları
SECRET_KEY = "mysecretkey"  # Güvenli bir şekilde saklayın
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise UserNotFoundError("Invalid token")
