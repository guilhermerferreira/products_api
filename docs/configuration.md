# Configuração do Projeto

## Arquivo `.env`

As configurações são carregadas pela classe `Settings`, localizada em `products_api/core/settings.py`.

```python
class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = 'HS256'
    JWT_EXPIRATION_MINUTES: int = 30
```

## Variáveis

| Variável | Obrigatória | Padrão | Descrição |
| --- | --- | --- | --- |
| `DATABASE_URL` | Sim | Nenhum | URL SQLAlchemy do banco de dados assíncrono |
| `JWT_SECRET_KEY` | Sim | Nenhum | Chave usada para assinar e validar tokens JWT |
| `JWT_ALGORITHM` | Não | `HS256` | Algoritmo de assinatura JWT |
| `JWT_EXPIRATION_MINUTES` | Não | `30` | Tempo de expiração do token em minutos |

## Banco de Dados

O engine assíncrono é criado em `products_api/core/database.py`:

```python
engine = create_async_engine(Settings().DATABASE_URL)
```

A sessão é fornecida por dependency injection do FastAPI:

```python
async def get_session():
    async with AsyncSession(engine, expire_on_commit=False) as session:
        yield session
```

## Alembic

O Alembic usa `migrations/env.py` para carregar a URL real do banco a partir do `.env`:

```python
config.set_main_option('sqlalchemy.url', Settings().DATABASE_URL)
target_metadata = Base.metadata
```

## MkDocs

A documentação usa MkDocs Material, configurado em `mkdocs.yml`.

Comandos úteis:

```bash
poetry run task docs
poetry run mkdocs serve
poetry run mkdocs build
```

