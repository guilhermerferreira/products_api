from datetime import datetime, timedelta, timezone
from typing import Dict, Optional

import jwt
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from pwdlib import PasswordHash

from products_api.core.settings import Settings
from products_api.models import User
from products_api.core.database import get_session


pwd_context = PasswordHash.recommended()
security = HTTPBearer()
settings = Settings()


def get_password_hash(password: str) -> str:
    '''Recebe uma senha e devolve a mesma criptografada'''
    return pwd_context.hash(password)  # hash() criptografa a senha


def verify_password(plain_password: str, hashed_password: str) -> bool:
    ''' Recebe uma senha descriptografada e compara com a criptografada
        se for igual retorna True
    '''
    return pwd_context.verify(plain_password, hashed_password) # verify() faz a comparação


def create_access_token(data: Dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.JWT_EXPIRATION_MINUTES
    )

    to_encode.update({'exp': expire})

    jwt_encoded = jwt.encode(
        to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )

    return jwt_encoded


def verify_token(token: str) -> Dict:
    try:
        payload = jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Token has expired',
            headers={'WWW-Authenticate': 'Bearer'}
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credentials',
            headers={'WWW-Authenticate': 'Bearer'}
        )


async def authenticate_user(
    email: str, password: str, db: AsyncSession
) -> Optional[User]:
    
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()

    if not user:
        return None
    
    if not verify_password(password, user.password):
        return None
    
    return user

