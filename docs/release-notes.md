# Release Notes

## 0.1.0

Data de referência: 2026-05-03.

### Adicionado

- Estrutura inicial da aplicação FastAPI.
- Health check em `GET /`.
- CRUD de usuários.
- Autenticação com JWT Bearer.
- Refresh de token.
- CRUD de marcas protegido por autenticação.
- CRUD de produtos protegido por autenticação.
- Validação de proprietário para buscar, atualizar e remover produtos.
- Modelos SQLAlchemy para `User`, `Brand` e `Product`.
- Enums de produto:
  - `ProductStatus`: `in_stock`, `out_of_stock`;
  - `ProductCondition`: `new`, `used`, `refurbished`.
- Migração inicial Alembic.
- Configuração por `.env`.
- Tasks de desenvolvimento com Taskipy.
- Documentação com MkDocs Material.

### Observações

- A pasta `tests/` existe, mas ainda não possui testes automatizados implementados.
- O projeto é descrito como uma API para estudo e prática de backend com Python.
