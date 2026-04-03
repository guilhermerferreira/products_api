from typing import Optional, List

from datetime import datetime
from pydantic import BaseModel, EmailStr, ConfigDict ,field_validator


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str

    @field_validator('username') # @field_validator() - cria uma validação
    def username_min_length(cls, v): # cls - própria classe
        if len(v) < 3:
            raise ValueError('Username deve ter pelo menos 3 caracteres')
        return v
    
    @field_validator('password')
    def password_min_length(cls, v):
        if len(v) < 6:
            raise ValueError('Password deve conter pelo menos 6 caracteres')
        return v   


class UserUpdateSchema(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

    @field_validator('username') # @field_validator() - cria uma validação
    def username_min_length(cls, v): # cls - própria classe
        if len(v) < 3:
            raise ValueError('Username deve ter pelo menos 3 caracteres')
        return v
    
    @field_validator('password')
    def password_min_length(cls, v):
        if len(v) < 6:
            raise ValueError('Password deve conter pelo menos 6 caracteres')
        return v   


class UserPublicSchema(BaseModel):
    model_config= ConfigDict(from_attributes=True) # Faz que seja possvel construir um UserPublicSchema, atráves de outros objetos
    
    id: int
    username: str
    email: EmailStr


class UserListPublicSchema(BaseModel):
    users: List[UserPublicSchema]
    offset: int
    limit: int
    created_at: datetime
    updated_at: datetime
