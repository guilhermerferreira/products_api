"""Adicionando novos campos a tabela product, e melhorias na tabela user

Revision ID: ae030377feac
Revises: d9b0c642b429
Create Date: 2026-04-08 18:15:40.297514

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'ae030377feac'
down_revision: Union[str, Sequence[str], None] = 'd9b0c642b429'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


import sqlalchemy as sa
from alembic import op

# 🔥 Define os ENUMs
product_status_enum = sa.Enum(
    'ACTIVE',
    'INACTIVE',
    'OUT_OF_STOCK',
    name='product_status_enum'
)

product_condition_enum = sa.Enum(
    'NEW',
    'USED',
    'REFURBISHED',
    name='product_condition_enum'
)


def upgrade() -> None:
    """Upgrade schema."""

    # ✅ cria os ENUMs no banco
    product_status_enum.create(op.get_bind())
    product_condition_enum.create(op.get_bind())

    # ✅ adiciona colunas
    op.add_column('products', sa.Column('status', product_status_enum, nullable=False))
    op.add_column('products', sa.Column('condition', product_condition_enum, nullable=False))
    op.add_column('products', sa.Column('is_available', sa.Boolean(), nullable=False, server_default=sa.text('true')))
    op.add_column('products', sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False))
    # ✅ index
    op.create_index(op.f('ix_products_status'), 'products', ['status'], unique=False)
    # nome da constraint (boa prática)
    op.create_unique_constraint('uq_products_name', 'products', ['name'])

    # remove colunas antigas
    op.drop_column('products', 'updated_At')
    op.drop_column('products', 'is_avaibled')


def downgrade() -> None:
    """Downgrade schema."""

    # recria colunas antigas
    op.add_column('products', sa.Column('is_avaibled', sa.Boolean(), nullable=False))
    op.add_column('products', sa.Column('updated_At', sa.DateTime(), server_default=sa.text('now()'), nullable=False))

    # remove novas
    op.drop_constraint('uq_products_name', 'products', type_='unique')
    op.drop_index(op.f('ix_products_status'), table_name='products')

    op.drop_column('products', 'updated_at')
    op.drop_column('products', 'is_available')
    op.drop_column('products', 'condition')
    op.drop_column('products', 'status')

    #  remove ENUMs do banco
    product_condition_enum.drop(op.get_bind())
    product_status_enum.drop(op.get_bind())
