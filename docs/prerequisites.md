# Pré-requisitos

## Ambiente

- Python `>=3.13,<4`
- Poetry compatível com `pyproject.toml`
- Banco de dados compatível com SQLAlchemy assíncrono
- Alembic para migrações

## Dependências Principais

As dependências são gerenciadas pelo Poetry:

- `fastapi[standard]`
- `sqlalchemy[asyncio]`
- `alembic`
- `pydantic-settings`
- `pwdlib[argon2]`
- `pyjwt`
- `aiosqlite`
- `asyncpg`
- `mkdocs`
- `mkdocs-material`
- `pymdown-extensions`

## Dependências de Desenvolvimento

- `ruff`
- `taskipy`

## Banco de Dados

O projeto lê a URL do banco pela variável `DATABASE_URL`. Exemplos:

```env
DATABASE_URL=sqlite+aiosqlite:///products.db
```

```env
DATABASE_URL=postgresql+asyncpg://usuario:senha@localhost:5432/products_api
```

## Variáveis Obrigatórias

O arquivo `.env` precisa conter, no mínimo:

```env
DATABASE_URL=sqlite+aiosqlite:///products.db
JWT_SECRET_KEY=troque-este-segredo
JWT_ALGORITHM=HS256
JWT_EXPIRATION_MINUTES=30
```

