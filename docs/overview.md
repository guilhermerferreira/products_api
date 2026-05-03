# Visão Geral do Projeto

A **Products API** é uma API REST assíncrona construída com FastAPI para praticar conceitos de backend em Python, incluindo validação de dados, persistência relacional, migrações de banco, autenticação JWT e organização modular por camadas.

## Objetivos

- Permitir criação, listagem, busca, atualização e remoção de usuários.
- Permitir autenticação por e-mail e senha com geração de token JWT.
- Permitir criação, listagem, busca, atualização e remoção de marcas.
- Permitir criação, listagem, busca, atualização e remoção de produtos, com relacionamento com marca e vendedor.
- Proteger operações sensíveis com autenticação Bearer.
- Restringir acesso a detalhes, atualização e remoção de produtos ao vendedor proprietário.

## Principais Recursos

- API HTTP com FastAPI.
- Banco de dados acessado por SQLAlchemy `asyncio`.
- Configuração por variáveis de ambiente via `pydantic-settings`.
- Migrações com Alembic.
- Senhas armazenadas com hash usando `pwdlib`.
- Tokens JWT assinados com segredo configurável.
- Documentação técnica com MkDocs Material.

## Domínios

| Domínio | Responsabilidade |
| --- | --- |
| Autenticação | Login, emissão e renovação de tokens JWT |
| Usuários | Cadastro e manutenção de contas de usuário |
| Marcas | Cadastro e manutenção de marcas associadas aos produtos |
| Produtos | Cadastro e manutenção de produtos, incluindo estoque, preço, condição e vendedor |

## Prefixos da API

| Prefixo | Domínio |
| --- | --- |
| `/api/v1/auth` | Autenticação |
| `/api/v1/users` | Usuários |
| `/api/v1/brands` | Marcas |
| `/api/v1/products` | Produtos |

