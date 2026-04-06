from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel, field_validator, ConfigDict


class BrandSchema(BaseModel):
    name: str
    description: Optional[str] = None
    is_active: bool = True

    @field_validator('name')
    def name_min_length(cls, v):
        if len(v.strip()) < 3:
            raise ValueError('Nome da marca deve ter pelo menos 3 caracteres')
        return v.strip()
        
    
class BrandPublicSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    name: str
    description: Optional[str]
    is_active: bool
    created_at: datetime
    updated_at: datetime

    @field_validator('name')
    def name_min_length(cls, v):
        if len(v.strip()) < 3:
            raise ValueError('Nome da marca deve ter pelo menos 3 caracteres')
        return v.strip()
    

class BrandUpdateSchema(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None

    @field_validator('name')
    def name_min_length(cls, v):
        if len(v.strip()) < 3:
            raise ValueError('Nome da marca deve ter pelo menos 3 caracteres')
        return v.strip()
    

class BrandListPublicSchema(BaseModel):
    brands: List[BrandSchema]

