import uuid
from passlib.context import CryptContext
from pydantic import EmailStr, Field, BaseModel
from datetime import datetime


class User(BaseModel):
    id: str = None
    name: str = Field(..., min_length=3, max_length=50)
    email: EmailStr = Field(..., error_msg='O email informado é inválido')
    telephone: str = Field(..., min_length=8)
    created_at: datetime = None

    class Config:
        orm_mode = True


class UserAdmin(User):
    password: str = Field(..., min_length=8)


class LoginData(BaseModel):
    email: EmailStr = Field(..., error_msg='O email informado é inválido')
    password: str = Field(..., min_length=8)


class Token(BaseModel):
    access_token: str
    token_type: str = Field(default='bearer')


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)
