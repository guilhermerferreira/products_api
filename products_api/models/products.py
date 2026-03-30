from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING, List

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Integer, Text, Numeric, func

from products_api.models import Base, User

if TYPE_CHECKING:
    from products_api.models import User

class Brand(Base):
    ''' Tabela de marcas '''
    __tablename__ = 'brands'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    is_active: Mapped[bool] = mapped_column(default=True)
    description: Mapped[str] = mapped_column(Text, default=None)
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        onupdate=func.now(),
        server_default=func.now()
    )

    products: Mapped[List['Product']] = relationship(
        'Product',
        back_populates='brand'
    )


class Product(Base):
    ''' Tabela de Produtos '''
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(Text, default=None)

    price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    stock: Mapped[int] = mapped_column(Integer)

    brand_id: Mapped[int] = mapped_column(ForeignKey('brands.id'))

    owner_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now()
    )
    updated_At: Mapped[datetime] = mapped_column(
        onupdate=func.now(),
        server_default=func.now()
    )
    is_avaibled: Mapped[bool] = mapped_column(default=True)

    brand: Mapped['Brand'] = relationship(
        'Brand',
        back_populates='products'
    )
    owner: Mapped['User'] = relationship(
        'User',
        back_populates='products'
    )
