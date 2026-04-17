# Products API

# API simples feita com FastAPI para estudo de backend em Python.

# Tecnologias
# Poetry
# Python
# pwdlib
# pydantic
# FastAPI
# SQLAlchemy
# Alembic
# PostgreSQL - asyncpg

# O que o projeto faz
# Criar usuários, lista, atualiza e remove
# Cria  marcas, lista, atualiza e remove
# Cria produtos, lista, atualiza e remove

# Como rodar
# 1. Clonar o projeto

# git clone https://github.com/guilhermerferreira/products_api.git
# cd products_api

# 2. Instalar dependências

# poetry install

# 3. Ativar o ambiente

# poetry shell

# 4. Criar o .env

# DATABASE_URL=sqlite+aiosqlite:///products.db

# 5. Rodar as migrations

# alembic upgrade head

# 6. Rodar o servidor

# uvicorn app.main --reload

# Acessar no navegador

# http://127.0.0.1:8000/docs

# Observações

# sse projeto foi feito para aprendizado e prática com FastAPI e banco de dados.

# Autor

# Guilherme Rodrigues
# https://www.linkedin.com/in/guilherme-rodrigues-ferreira-306876356/