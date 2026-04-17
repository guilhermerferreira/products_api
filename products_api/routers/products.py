from typing import Optional

from fastapi import APIRouter, Depends, status, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, exists
from sqlalchemy.orm import selectinload

from products_api.models import Product, User, Brand
from products_api.models.products import ProductCondition, ProductStatus
from products_api.core.database import get_session
from products_api.schemas.products import(
    ProductSchema,
    ProductPublicSchema,
    ProductListPublicSchema,
    ProductUpdateSchema
)


router = APIRouter()


@router.post(
    path='/',
    status_code=status.HTTP_201_CREATED,
    response_model=ProductPublicSchema,
    summary='Criar produto'
)
async def create_product(
    product: ProductSchema,
    db: AsyncSession = Depends(get_session)
):  
    name_exists = await db.scalar(
        select(exists().where(Product.name == product.name))
    )
    if name_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Nome do produto já em uso'
        )

    brand_exists = await db.scalar(
        select(exists().where(Brand.id == product.brand_id))
    )
    if not brand_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Marca não encontrada',
        )
    
    seller_exists = await db.scalar(
        select(exists().where(User.id == product.seller_id))
    )
    if not seller_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Proprietário não encontrado',
        )
    

    db_product = Product(
        name = product.name,
        description = product.description,
        price = product.price,
        stock = product.stock,
        status = product.status,
        condition = product.condition,
        is_available = product.is_available,
        brand_id = product.brand_id,
        seller_id = product.seller_id_id,
    )

    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)

    result = await db.execute(
        select(Product)
        .options(selectinload(Product.brand), selectinload(Product.seller))
        .where(Product.id == db_product.id)
    )
    product_with_relations = result.scalar_one()

    return product_with_relations


@router.get(
    path='/',
    status_code=status.HTTP_200_OK,
    response_model=ProductListPublicSchema,
    summary='Listar produtos',
)
async def list_products(
    offset: int = Query(0, ge=0, description=('Número de registros para pular')),
    limit: int = Query(100, ge=1, le=100, description=('Limite de registros')),
    search: Optional[str] = Query(None, description=('Buscar produto por nome')),
    brand_id: Optional[int] = Query(None, description=('Filtrar por marca')),
    seller_id: Optional[int] = Query(None, description=('Filtrar por vendedor')),
    condition: Optional[ProductCondition] = Query(None, description=('Filtrar produto pela condição')),
    status: Optional[ProductStatus] = Query(None, description=('Filtrar produto pelos status(em estoque/sem estoque)')),
    is_available: Optional[bool] = Query(None, description=('Filtrar por disponibilidade')),
    min_price: Optional[float] = Query(None, description=('Preço mínimo')),
    max_price: Optional[float] = Query(None, description=('Preço máximo')),
    db: AsyncSession = Depends(get_session)
):
    query = select(Product).options(selectinload(Product.brand), selectinload(Product.seller))

    if search:
        search_filter = f'%{search}%'
        query = query.where(Product.name.ilike(search_filter))

    if brand_id is not None:
        query = query.where(Product.brand_id == brand_id)

    if seller_id is not None:
        query = query.where(Product.seller_id == seller_id)

    if condition is not None:
        query = query.where(Product.condition == condition)

    if status is not None:
        query = query.where(Product.status == status)

    if is_available is not None:
        query = query.where(Product.is_available == is_available)

    if min_price is not None:
        query = query.where(Product.price >= min_price)

    if max_price is not None:
        query = query.where(Product.price <= max_price)

    query = query.offset(offset).limit(limit)

    result = await db.execute(query)
    products = result.scalars().all()

    return {'products': products, 'offset': offset, 'limit': limit}


@router.get(
    path='/{product_id}',
    status_code=status.HTTP_200_OK,
    response_model=ProductPublicSchema,
    summary='Buscar produto por ID',
)
async def get_product(
    product_id: int,
    db: AsyncSession = Depends(get_session),
):
    result = await db.execute(
        select(Product)
        .options(selectinload(Product.brand), selectinload(Product.seller))
        .where(Product.id == product_id)
    )
    product = result.scalar_one_or_none()

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Produto não encontrado'
        )

    return product


@router.put(
    path='/{product_id}',
    status_code=status.HTTP_200_OK,
    response_model=ProductPublicSchema,
    summary='Atualizar produto'
)
async def update_product(
    product_id: int,
    product_update: ProductUpdateSchema,
    db: AsyncSession = Depends(get_session)
):
    product = await db.get(Product, product_id)

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Produto não encontrado',
        )

    update_data = product_update.model_dump(exclude_unset=True)        

    if 'name' in update_data and update_data['name'] != product.name:
        name_exists = await db.scalar(
        select(exists().where( (Product.name == update_data['name']) & (Product.id != product_id) )) 
    )
        if name_exists:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Nome do produto já em uso'
            )
    
    if 'brand_id' in update_data and update_data['brand_id'] != product.brand_id:
        brand_exists = await db.scalar(
        select(exists().where(Brand.id == update_data['brand_id']))
    )
        if not brand_exists:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Marca não encontrada',
            )

    if 'seller_id' in update_data and update_data['seller_id'] != product.seller_id:
        seller_exists = await db.scalar(
        select(exists().where(User.id == update_data['seller_id']))
    )
        if not seller_exists:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Proprietário não encontrado',
            )

    for field, value in update_data.items():
        setattr(product, field, value)
    
    await db.commit()
    await db.refresh(product)

    result = await db.execute(
        select(Product)
        .options(selectinload(Product.brand), selectinload(Product.seller))
        .where(Product.id == product_id)
    )
    product_with_relations = result.scalar_one()

    return product_with_relations


@router.delete(
    path='/{product_id}',
    status_code=status.HTTP_204_NO_CONTENT,
    summary='Deletar produto',
)
async def delete_product(
    product_id: int,
    db: AsyncSession = Depends(get_session)
):
    product = await db.get(Product, product_id)

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Produto não encontrado',
        )
    
    await db.delete(product)
    await db.commit()

    return 