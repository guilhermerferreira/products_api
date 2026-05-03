# Guidelines e Padrões

## Organização Geral

- `products_api/app.py` registra a aplicação FastAPI e os routers.
- `products_api/routers/` concentra endpoints HTTP.
- `products_api/schemas/` concentra contratos Pydantic de entrada e saída.
- `products_api/models/` concentra modelos SQLAlchemy e relacionamentos.
- `products_api/core/` concentra infraestrutura compartilhada, como segurança, banco e settings.
- `migrations/` concentra versionamento do schema do banco.

## Convenções de Código

- Usar funções assíncronas (`async def`) para endpoints e operações de banco.
- Usar `AsyncSession` via `Depends(get_session)`.
- Usar schemas Pydantic para validar payloads e formatar respostas.
- Usar SQLAlchemy ORM para consultas e persistência.
- Retornar erros HTTP explícitos com `HTTPException`.
- Aplicar hash em senhas antes de persistir no banco.
- Proteger endpoints sensíveis com `Depends(get_current_user)`.

## Formatação e Lint

O projeto configura Ruff em `pyproject.toml`.

Comandos:

```bash
poetry run task lint
poetry run task format
```

## Padrões de API

- Prefixo versionado: `/api/v1`.
- Rotas agrupadas por domínio.
- Paginação por `offset` e `limit`.
- Filtros via query parameters.
- Respostas públicas sem expor a senha do usuário.

## Padrões de Segurança

- Nunca armazenar senha em texto puro.
- Nunca versionar `.env` com segredos reais.
- Usar `Authorization: Bearer <token>` para endpoints autenticados.
- Validar ownership antes de permitir acesso, atualização ou remoção de produtos.

## Migrações

- Alterações em modelos devem gerar nova revision Alembic.
- Revisar migrations antes de aplicar em ambientes compartilhados.
- Aplicar migrations com:

```bash
poetry run alembic upgrade head
```

