from pydantic import EmailStr, Field, BaseModel, validator
from datetime import datetime


class User(BaseModel):
    id: str = None
    name: str = Field(min_length=3, max_length=50)
    email: EmailStr
    telephone: str = Field(min_length=8, max_length=15)
    created_at: datetime = None

    class Config:
        orm_mode = True


class UserAdmin(User):
    password: str

    @validator('password')
    def validate_password(v):
        if len(v) < 8:
            raise ValueError('A senha deve ter pelo menos 8 caracteres')
        if not any(char.isupper() for char in v):
            raise ValueError('A senha deve conter pelo menos uma letra maiúscula')
        if not any(char.islower() for char in v):
            raise ValueError('A senha deve conter pelo menos uma letra minúscula')
        if not any(char.isdigit() for char in v):
            raise ValueError('A senha deve conter pelo menos um número')
        return v


class LoginData(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)


class Token(BaseModel):
    access_token: str
    token_type: str = Field(default='bearer')

