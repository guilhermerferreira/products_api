# Testes

## Estado Atual

A pasta `tests/` existe, mas ainda não há testes implementados além de `tests/__init__.py`.

## Como Executar

O projeto ainda não declara `pytest` nas dependências. Quando os testes forem adicionados, recomenda-se incluir dependências de teste no grupo de desenvolvimento:

```bash
poetry add --group dev pytest pytest-asyncio httpx
```

Execução esperada:

```bash
poetry run pytest
```

## Estratégia Recomendada

- Testes unitários para validações dos schemas.
- Testes unitários para funções de segurança:
  - hash de senha;
  - verificação de senha;
  - criação e validação de token;
  - tratamento de token expirado ou inválido.
- Testes de integração para endpoints usando cliente HTTP assíncrono.
- Banco isolado para testes, preferencialmente SQLite assíncrono ou container PostgreSQL.
- Testes de autorização para garantir que um vendedor não altere produtos de outro vendedor.

## Casos Prioritários

| Área | Caso |
| --- | --- |
| Usuários | Criar usuário com e-mail único |
| Usuários | Bloquear username duplicado |
| Auth | Login com credenciais válidas |
| Auth | Login com senha inválida |
| Marcas | Criar marca autenticado |
| Marcas | Bloquear marca duplicada |
| Produtos | Criar produto com marca e vendedor existentes |
| Produtos | Bloquear produto com marca inexistente |
| Produtos | Bloquear acesso a produto de outro vendedor |

## Qualidade

Antes de abrir uma alteração, rode:

```bash
poetry run task lint
poetry run task format
poetry run pytest
```

Enquanto `pytest` não estiver configurado no projeto, registre no pull request que a validação automatizada está limitada a lint e formatação.

