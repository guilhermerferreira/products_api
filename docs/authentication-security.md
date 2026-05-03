# Autenticação e Segurança

## Autenticação

A autenticação é baseada em JWT Bearer.

Fluxo principal:

1. O cliente envia `email` e `password` para `POST /api/v1/auth/token`.
2. A API busca o usuário pelo e-mail.
3. A senha enviada é comparada com o hash salvo no banco.
4. A API gera um token JWT com `sub` igual ao ID do usuário.
5. O cliente envia o token em endpoints protegidos.

Header esperado:

```http
Authorization: Bearer <access_token>
```

## Hash de Senha

As senhas são processadas por `pwdlib.PasswordHash.recommended()`.

Funções principais:

- `get_password_hash(password)`: gera o hash antes de salvar.
- `verify_password(plain_password, hashed_password)`: valida login.

## Token JWT

O token é criado com:

- `sub`: ID do usuário.
- `exp`: data de expiração.
- `JWT_SECRET_KEY`: chave de assinatura.
- `JWT_ALGORITHM`: algoritmo, por padrão `HS256`.

## Usuário Atual

A dependency `get_current_user`:

- Lê credenciais Bearer.
- Valida assinatura e expiração do token.
- Extrai `sub`.
- Busca o usuário no banco.
- Retorna o usuário autenticado para o endpoint.

## Autorização por Proprietário

Produtos possuem `seller_id`.

Em busca por ID, atualização e remoção de produtos, a função `verify_product_seller` compara:

```text
current_user.id == product.seller_id
```

Se o usuário autenticado não for o vendedor do produto, a API retorna `403 Forbidden`.

## Endpoints Públicos e Protegidos

| Recurso | Público | Protegido |
| --- | --- | --- |
| Health check | `GET /` | Nenhum |
| Auth | `POST /api/v1/auth/token` | `POST /api/v1/auth/refresh_token` |
| Users | `POST`, `GET`, `GET /{id}` | `PUT`, `DELETE` |
| Brands | Nenhum | Todos |
| Products | Nenhum | Todos |

## Cuidados Operacionais

- Usar `JWT_SECRET_KEY` forte em produção.
- Não versionar `.env` com segredos reais.
- Preferir HTTPS em produção.
- Definir tempo de expiração coerente com o risco do ambiente.
- Rotacionar segredos se houver exposição.

