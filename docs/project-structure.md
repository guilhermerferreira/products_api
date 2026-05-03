# Estrutura do Projeto

```text
.
├── README.md
├── pyproject.toml
├── poetry.lock
├── alembic.ini
├── mkdocs.yml
├── docs/
├── migrations/
├── products_api/
└── tests/
```

## Raiz

| Caminho | Descrição |
| --- | --- |
| `README.md` | Apresentação resumida do projeto |
| `pyproject.toml` | Metadados, dependências e tasks |
| `poetry.lock` | Versões travadas das dependências |
| `alembic.ini` | Configuração base do Alembic |
| `mkdocs.yml` | Configuração da documentação |
| `.env` | Variáveis locais de ambiente, não deve ser versionado |

## Aplicação

```text
products_api/
├── __init__.py
├── app.py
├── core/
├── models/
├── routers/
└── schemas/
```

| Caminho | Descrição |
| --- | --- |
| `products_api/app.py` | Cria a instância FastAPI e registra routers |
| `products_api/core/settings.py` | Carrega configurações via `.env` |
| `products_api/core/database.py` | Cria engine e sessão assíncrona |
| `products_api/core/security.py` | Hash de senha, JWT e validação de usuário atual |
| `products_api/models/base.py` | Classe base declarativa do SQLAlchemy |
| `products_api/models/users.py` | Modelo `User` |
| `products_api/models/products.py` | Modelos `Brand`, `Product` e enums |
| `products_api/routers/auth.py` | Endpoints de autenticação |
| `products_api/routers/users.py` | Endpoints de usuários |
| `products_api/routers/brands.py` | Endpoints de marcas |
| `products_api/routers/products.py` | Endpoints de produtos |
| `products_api/schemas/*.py` | Schemas Pydantic de entrada e saída |

## Migrações

```text
migrations/
├── env.py
├── README
├── script.py.mako
└── versions/
    └── 031f120a9c1b_initial_schema.py
```

## Testes

```text
tests/
└── __init__.py
```

A pasta de testes existe, mas ainda não possui testes implementados.

