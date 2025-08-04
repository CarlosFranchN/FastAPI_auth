from sqlalchemy.orm import Session
from sqlalchemy import select

from fastapi import HTTPException, status
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import JWTError, jwt

from app.models.user import User
from app.schemas.user import UserCreate
from passlib.context import CryptContext
from app.core.config import settings
from app.db.sessions import get_db


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oAuth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/token')

def create_user(db: Session, user_data: UserCreate) -> User:
    statement = select(User).where(User.email == user_data.email)
    
    db_user = db.execute(statement).scalar_one_or_none()
    print(db_user)
    # db_user = db.query(User).filter(User.email == user_data.email).first()
    
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email ja foi registrado!"
        )
    
    hashed_password = pwd_context.hash(user_data.password)
    db_user = User(
        email = user_data.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    # db.flush()
    db.refresh(db_user)
    
    return db_user

def verify_password(plain_password:str , hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(db: Session, email:str , password: str) -> Optional[User]:
    # user = db.query(User).filter(User.email == email).first()
    statement = select(User).where(User.email == email)
    user = db.execute(statement).scalar_one_or_none()
    
    if not user:
        return None
    
    if not verify_password(password, user.hashed_password):
        return None
    
    return user

def create_access_token(data:dict) -> str:
    to_encode = data.copy()
    
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp" : expire})
    
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGOTITHM)
    
    return encoded_jwt

def get_current_user(
    token: str = Depends(oAuth2_scheme),
    db: Session  = Depends(get_db)
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credencial não autorizada",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGOTITHM]
        )
        email: str = payload.get('sub')
        if not email:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    statement = select(User).where(User.email == email)
    user = db.execute(statement).scalar_one_or_none()
    
    
    if not user:
        raise credentials_exception
    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Usuario Inativo!")
    return user