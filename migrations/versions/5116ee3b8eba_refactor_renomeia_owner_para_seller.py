"""refactor: renomeia owner para seller

Revision ID: 5116ee3b8eba
Revises: ae030377feac
Create Date: 2026-04-16 18:48:51.615504

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5116ee3b8eba'
down_revision: Union[str, Sequence[str], None] = 'ae030377feac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1. Atualiza dados do ENUM
    op.execute("""UPDATE products SET status = 'IN_STOCK' WHERE status = 'ACTIVE'""")
    op.execute("""UPDATE products SET status = 'OUT_OF_STOCK' WHERE status = 'INACTIVE'""")
    # 2. Remove FK antiga
    op.drop_constraint('products_owner_id_fkey', 'products', type_='foreignkey')
    # 3. Rename da coluna
    op.alter_column('products', 'owner_id', new_column_name='seller_id')
    # 4. Cria nova FK
    op.create_foreign_key(
        'products_seller_id_fkey',
        'products',
        'users',
        ['seller_id'],
        ['id']
    )
    # 5. Ajusta ENUM (PostgreSQL)
    op.execute("ALTER TYPE product_status_enum RENAME TO product_status_enum_old")
    op.execute("""CREATE TYPE product_status_enum AS ENUM ('IN_STOCK', 'OUT_OF_STOCK')""")
    op.execute("""
        ALTER TABLE products
        ALTER COLUMN status TYPE product_status_enum
        USING status::text::product_status_enum
    """)
    op.execute("DROP TYPE product_status_enum_old")


def downgrade() -> None:
    # 1. Volta ENUM antigo
    op.execute("""CREATE TYPE product_status_enum_old AS ENUM ('ACTIVE', 'INACTIVE')""")
    op.execute("""
        ALTER TABLE products
        ALTER COLUMN status TYPE product_status_enum_old
        USING status::text::product_status_enum_old
    """)
    op.execute("DROP TYPE product_status_enum")
    op.execute("ALTER TYPE product_status_enum_old RENAME TO product_status_enum")
    # 2. Remove FK nova
    op.drop_constraint('products_seller_id_fkey', 'products', type_='foreignkey')
    # 3. Rename reverso
    op.alter_column('products', 'seller_id', new_column_name='owner_id')
    # 4. Cria FK antiga
    op.create_foreign_key(
        'products_owner_id_fkey',
        'products',
        'users',
        ['owner_id'],
        ['id']
    )
