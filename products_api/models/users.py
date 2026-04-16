from datetime import datetime
from typing import TYPE_CHECKING, List

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import func, String

from products_api.models import Base

if TYPE_CHECKING:
    from products_api.models import Product

class User(Base):
    __tablename__ = 'users'

    
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    
    password: Mapped[str]
    
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        onupdate=func.now(),
        server_default=func.now(),
    )

    products: Mapped[List['Product']] = relationship(
        'Product',
        back_populates='seller',
    )