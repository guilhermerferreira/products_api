from typing import Optional

from fastapi import APIRouter, status, Depends, HTTPException, Query

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import  select, exists

from products_api.core.database import get_session
from products_api.core.security import get_password_hash
from products_api.db import USERS
from products_api.models import User
from products_api.schemas.users import UserPublicSchema, UserSchema, UserListPublicSchema, UserUpdateSchema 


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
        password = get_password_hash(user.password),
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
async def list_users(
    offset: int = Query(0, ge=0, description='Número de registros para pular'),
    limit: int = Query(100, ge=1, description='Limite de registros'),
    search: Optional[str] = Query(None, description='Buscar por username ou email'),
    db: AsyncSession = Depends(get_session),
):
    query = select(User)

    if search:
        search_filter = f'%{search}%'
        query = query.where(
            (User.username.ilike(search_filter))
            | (User.email.ilike(search_filter))
        )

    query = query.offset(offset).limit(limit)

    result = await db.execute(query)
    users = result.scalars().all()

    return {'users': users, 'offset': offset, 'limit': limit}


@routers.get(
    path='/{user_id}', 
    status_code=status.HTTP_200_OK,
    response_model= UserPublicSchema,
    summary='Buscar usuário pelo ID'
)
async def get_user(
    user_id: int,
    db: AsyncSession = Depends(get_session)
):
    user = await db.get(User, user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Usuário não encontrado',
        )
    
    return user


@routers.put(
    path='/{user_id}', 
    status_code=status.HTTP_201_CREATED, 
    response_model=UserPublicSchema,
    summary='Atualizar usuário'
)
async def update_user(
    user_id: int, 
    user_update: UserUpdateSchema,
    db: AsyncSession = Depends(get_session)
):
    user = await db.get(User, user_id)

    if not user: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Usuário não encontrado',
        )
    
    update_data = user_update.model_dump(exclude_unset=True)

    if 'username' in update_data and update_data['username'] != user.username:
        username_exists = await db.scalar(
            select(exists().where(
                (User.username == update_data['username']) &
                (User.id != user_id)
            ))        
        )
        if username_exists:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Username já em uso',
            )

    if 'email' in update_data and update_data['email'] != user.email:
        email_exists = await db.scalar(
            select(exists().where(
                (User.email == update_data['email']) &
                (User.id != user_id)
            ))
        )
        if email_exists:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='E-mail já em uso',
            )

    if 'password' in update_data['password']:
        update_data['password'] = get_password_hash(update_data['password'])

    for field, value in update_data.items():
        setattr(user, field, value) 

    await db.commit()
    await db.refresh(user)

    return user


@routers.delete(
    path='/{user_id}', 
    status_code=status.HTTP_204_NO_CONTENT,
    summary='Deletar usuário'
)
async def delete_user(
    user_id: int,
    db: AsyncSession = Depends(get_session)
):
    
    user = await db.get(User, user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Usuário não encontrado',
        )

    await db.delete(user)
    await db.commit()

    return 