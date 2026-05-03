# Instalação

## Clonar o Repositório

```bash
git clone https://github.com/guilhermerferreira/products_api.git
cd products_api
```

## Instalar Dependências

```bash
poetry install
```

## Ativar o Ambiente Virtual

```bash
poetry shell
```

Também é possível executar comandos sem ativar o shell:

```bash
poetry run fastapi dev products_api/app.py
```

## Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
DATABASE_URL=sqlite+aiosqlite:///products.db
JWT_SECRET_KEY=troque-este-segredo
JWT_ALGORITHM=HS256
JWT_EXPIRATION_MINUTES=30
```

## Executar Migrações

```bash
poetry run alembic upgrade head
```

## Iniciar a API

```bash
poetry run task run
```

O task `run` executa:

```bash
fastapi dev products_api/app.py
```

## Acessar a Documentação Interativa

Com o servidor rodando:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
- Health check: `http://127.0.0.1:8000/`

