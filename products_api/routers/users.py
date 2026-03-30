from fastapi import APIRouter, status, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import  select, exists

from products_api.schemas.users import UserPublicSchema, UserSchema, UserListPublicSchema 
from products_api.core.database import get_session
from products_api.models import User
from products_api.db import USERS


routers = APIRouter()


@routers.post(
    path='/',
    status_code=status.HTTP_201_CREATED,
    response_model=UserPublicSchema,
    summary='Criar novo usuário'
)
async def create_user(user: UserSchema, db: AsyncSession = Depends(get_session)):

    username_exist = await db.scalar(
        select(exists().where(User.username == user.username))
    )
    if username_exist:
        raise HTTPException(
            detail='Username já utilizado.'
        )

    email_exist = await db.scalar(
        select(exists().where(User.email == user.email))
    )
    if email_exist:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='E-mail já utilizado.'
        )

    db_user = User(
        username = user.username,
        email = user.email,
        password = user.password,
    )

    db.add(db_user) # add: adiciona algo ao banco
    await db.commit()  # salva no banco de dados, isso é um I/O por isso o await
    await db.refresh(db_user) # atualiza pegando o id gerado no banco
    
    return db_user

@routers.get(
    path='/',
    status_code=status.HTTP_200_OK, 
    response_model=UserListPublicSchema,
    summary='Listar usuários'
)
async def list_users():
    return {'users': USERS}


@routers.put(
    path='/{user_id}', 
    status_code=status.HTTP_201_CREATED, 
    response_model=UserPublicSchema,
    summary='Atualizar usuário'
)
async def update_user(user_id: int, user: UserSchema):
    user_with_id = UserPublicSchema(**user.model_dump(), id= user_id)
    USERS[user_id - 1] = user_with_id
    return user_with_id 


@routers.delete(
    path='/{user_id}', 
    status_code=status.HTTP_204_NO_CONTENT,
    summary='Deletar usuário'
)
async def delete_user(user_id: int):
    del USERS[user_id - 1]
    return 