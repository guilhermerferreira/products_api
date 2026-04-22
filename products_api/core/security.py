from datetime import datetime, timedelta, timezone
from typing import Dict

import jwt
from pwdlib import PasswordHash

from products_api.core.settings import Settings


pwd_context = PasswordHash.recommended()
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
    expire = datetime.now(timezone.utc()) + timedelta(
        minutes=settings.JWT_EXPIRED_MINUTES
    )

    to_encode.update({'exp': expire})

    jwt_encoded = jwt.encode(
        to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )

    return jwt_encoded

