# Products API

Bem-vindo à documentação da **Products API**, uma API REST desenvolvida com FastAPI para estudo e prática de backend em Python.

O projeto oferece recursos para cadastro, autenticação e gerenciamento de usuários, marcas e produtos. No domínio atual, os produtos podem ser tratados como carros quando aplicável às regras de negócio.

## Navegação

- [Visão Geral](overview.md)
- [Pré-requisitos](prerequisites.md)
- [Instalação](installation.md)
- [Configuração do Projeto](configuration.md)
- [Guidelines e Padrões](guidelines.md)
- [Estrutura do Projeto](project-structure.md)
- [API Endpoints](api-endpoints.md)
- [Modelagem do Sistema](system-modeling.md)
- [Autenticação e Segurança](authentication-security.md)
- [Desenvolvimento](development.md)
- [Testes](tests.md)
- [Deploy](deploy.md)
- [Contribuição](contribution.md)
- [Release Notes](release-notes.md)

## Resumo Técnico

| Item | Descrição |
| --- | --- |
| Linguagem | Python 3.13 |
| Framework | FastAPI |
| Banco de dados | SQLAlchemy assíncrono com URL configurável |
| Migrações | Alembic |
| Autenticação | JWT Bearer |
| Hash de senha | pwdlib com Argon2 |
| Documentação | MkDocs Material |

## Pontos de Entrada

- Aplicação FastAPI: `products_api/app.py`
- Configurações: `products_api/core/settings.py`
- Rotas: `products_api/routers/`
- Modelos SQLAlchemy: `products_api/models/`
- Schemas Pydantic: `products_api/schemas/`
- Migrações Alembic: `migrations/`

## Links Locais Úteis

Com a aplicação em execução:

- Health check: `GET /`
- Swagger UI: `/docs`
- ReDoc: `/redoc`

Com o MkDocs em execução:

- Documentação local: endereço configurado pelo comando `task docs` ou `mkdocs serve`
