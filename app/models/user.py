from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base,DeclarativeBase 
import datetime

class Base(DeclarativeBase):
    create_at = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc) )


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, 
                primary_key=True, 
                index=True)
    email = Column(String(255),
                   unique=True,
                   index=True,
                   nullable=False)
    hashed_password= Column(String(255),
                            nullable=False
                            )  
    is_active = Column(Boolean, default=True)
    
    def __repr__(self):
        return f"<User(id={self.id} , email={self.email})"