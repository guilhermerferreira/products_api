# Desenvolvimento

## Executar Localmente

```bash
poetry install
poetry run alembic upgrade head
poetry run task run
```

O comando `task run` inicia:

```bash
fastapi dev products_api/app.py
```

## Documentação Local

```bash
poetry run task docs
```

Ou:

```bash
poetry run mkdocs serve
```

## Fluxo Sugerido de Desenvolvimento

1. Criar ou atualizar models em `products_api/models/`.
2. Criar ou atualizar schemas em `products_api/schemas/`.
3. Implementar comportamento HTTP em `products_api/routers/`.
4. Registrar router em `products_api/app.py`, se for um novo domínio.
5. Gerar migration Alembic quando houver alteração no banco.
6. Rodar lint e testes.
7. Atualizar documentação quando o contrato da API mudar.

## Criar Migration

```bash
poetry run alembic revision --autogenerate -m "descricao da mudanca"
```

## Aplicar Migration

```bash
poetry run alembic upgrade head
```

## Reverter Última Migration

```bash
poetry run alembic downgrade -1
```

## Lint e Formatação

```bash
poetry run task lint
poetry run task format
```

## Rotas Interativas

Durante o desenvolvimento, use a documentação automática do FastAPI:

- `/docs`
- `/redoc`

