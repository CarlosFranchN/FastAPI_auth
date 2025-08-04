from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.db.sessions import get_db
from app.schemas.user import UserCreate,UserPublic
from app.services import auth_service
from app.models.user import User

router = APIRouter(tags=["Authentication"])

@router.post("/cadastro" , response_model=UserPublic , status_code=201)
def register_user(user: UserCreate , db: Session =Depends(get_db)):
    return auth_service.create_user(db=db, user_data=user)

@router.post("/token")
def login_for_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = auth_service.authenticate_user(
        db=db,
        email=form_data.username,
        password=form_data.password
    )
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Dados incorretos",
            headers={"WWW-Authenticate" : "Bearer"},
        )
    
    access_token = auth_service.create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, 
            "token_type" : "bearer"}
    
@router.get("/users/me" , response_model=UserPublic)
def read_user(current_user : User = Depends(auth_service.get_current_user)):
    return current_user