from passlib.context import CryptContext
from sqlalchemy.orm import Session
from app.domain.models import User
from app.infrastructure.auth import create_access_token
from app.domain.exceptions import UserAlreadyExistsError, UserNotFoundError

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def register_user(db: Session, email: str, name: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if user:
        raise UserAlreadyExistsError(email)
    hashed_password = hash_password(password)
    new_user = User(email=email, name=name, password_hash=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def login_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password_hash):
        raise UserNotFoundError(email)
    token_data = {"sub": user.email}
    token = create_access_token(data=token_data)
    return token
