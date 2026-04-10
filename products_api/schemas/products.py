from typing import Optional, List
from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, field_validator, ConfigDict


from products_api.models.products import ProductStatus, ProductCondition
from products_api.schemas.brands import BrandPublicSchema
from products_api.schemas.users import UserPublicSchema


class ProductSchema(BaseModel):
    name: str
    description: Optional[str] = None
    price: Decimal
    stock: int
    status: ProductStatus
    condition: ProductCondition
    is_available: bool = True
    brand_id: int
    owner_id: int

    @field_validator('name')
    def name_min_length(cls, v):
        if len(v.strip()) < 3:
            raise ValueError('Nome do produto deve conter pelo menos 3 caracteres')
        return v.strip()
    
    @field_validator('price')
    def price_validate(cls, v):
        if v <= 0:
            raise ValueError('O valor do produto deve ser maior que zero')
        return v

    @field_validator('stock')
    def stock_validate(cls, v):
        if v <= 0:
            raise ValueError('Estoque do produto deve ser maior que zero')
        return v


class ProductUpdateSchema(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[Decimal] = None
    stock: Optional[int] = None
    status: Optional[ProductStatus] = None
    condition: Optional[ProductCondition] = None
    is_available: Optional[bool] = None
    brand_id: Optional[int] = None
    owner_id: Optional[int] = None

    @field_validator('name')
    def name_min_length(cls, v):
        if v is None:
            return v
        if len(v.strip()) < 3:
            raise ValueError('Nome do produto deve conter pelo menos 3 caracteres')
        return v.strip()
    
    @field_validator('price')
    def price_validate(cls, v):
        if v is None:
            return v
        if v <= 0:
            raise ValueError('O valor do produto deve ser maior que zero')
        return v

    @field_validator('stock')
    def stock_validate(cls, v):
        if v is None:
            return v
        if v <= 0:
            raise ValueError('Estoque do produto deve ser maior que zero')
        return v
    

class ProductPublicSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True) # permite criar um CarPublicSchema a partir de outros objetos
    
    id: int
    name: str
    description: Optional[str] = None
    price: Decimal
    stock: int
    status: ProductStatus
    condition: ProductCondition
    is_available: bool = True
    brand_id: int
    owner_id: int    
    created_at: datetime
    updated_at: datetime
    brand: BrandPublicSchema
    owner: UserPublicSchema


class ProductListPublicSchema(BaseModel):
    products: List[ProductPublicSchema]
    offset: int
    limit: int

