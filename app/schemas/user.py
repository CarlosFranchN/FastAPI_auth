from pydantic import BaseModel, EmailStr, Field
from typing import Optional
class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(
        ...,
        description="A senha do usuario!",
        example="zezinho123"
    )
    
class UserPublic(BaseModel):
    id: int = Field(...)
    email: EmailStr = Field(..., example="doidinho@example.com")
    is_active: bool 
    
    model_config = {
        "from_attributes" : True
    }
    
class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(
        default= None,
        description="A senha do usuario!",
        example="zezinho123"
    )
    
class UserInDB(UserPublic):
    hashed_password: str