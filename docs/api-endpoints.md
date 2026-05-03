# API Endpoints

Base URL local padrão:

```text
http://127.0.0.1:8000
```

## Health Check

| Método | Caminho | Autenticação | Descrição |
| --- | --- | --- | --- |
| `GET` | `/` | Não | Retorna o status da aplicação |

Resposta:

```json
{
  "status": "ok"
}
```

## Autenticação

Prefixo: `/api/v1/auth`

| Método | Caminho | Autenticação | Descrição |
| --- | --- | --- | --- |
| `POST` | `/token` | Não | Autentica usuário e gera token JWT |
| `POST` | `/refresh_token` | Sim | Gera novo token para o usuário autenticado |

### `POST /api/v1/auth/token`

Payload:

```json
{
  "email": "user@example.com",
  "password": "123456"
}
```

Resposta:

```json
{
  "access_token": "jwt",
  "token_type": "bearer"
}
```

## Usuários

Prefixo: `/api/v1/users`

| Método | Caminho | Autenticação | Descrição |
| --- | --- | --- | --- |
| `POST` | `/` | Não | Cria usuário |
| `GET` | `/` | Não | Lista usuários |
| `GET` | `/{user_id}` | Não | Busca usuário por ID |
| `PUT` | `/{user_id}` | Sim | Atualiza usuário |
| `DELETE` | `/{user_id}` | Sim | Remove usuário |

### Campos de Criação

```json
{
  "username": "guilherme",
  "email": "gui@example.com",
  "password": "123456"
}
```

### Query Parameters de Listagem

| Parâmetro | Tipo | Descrição |
| --- | --- | --- |
| `offset` | `int` | Quantidade de registros ignorados, mínimo `0` |
| `limit` | `int` | Quantidade máxima de registros, mínimo `1` |
| `search` | `string` | Busca por `username` ou `email` |

## Marcas

Prefixo: `/api/v1/brands`

| Método | Caminho | Autenticação | Descrição |
| --- | --- | --- | --- |
| `POST` | `/` | Sim | Cria marca |
| `GET` | `/` | Sim | Lista marcas |
| `GET` | `/{brand_id}` | Sim | Busca marca por ID |
| `PUT` | `/{brand_id}` | Sim | Atualiza marca |
| `DELETE` | `/{brand_id}` | Sim | Remove marca |

### Campos de Criação

```json
{
  "name": "Toyota",
  "description": "Fabricante de veículos",
  "is_active": true
}
```

### Query Parameters de Listagem

| Parâmetro | Tipo | Descrição |
| --- | --- | --- |
| `offset` | `int` | Quantidade de registros ignorados |
| `limit` | `int` | Quantidade máxima de registros, entre `1` e `100` |
| `search` | `string` | Busca por nome |
| `is_active` | `bool` | Filtra marcas ativas ou inativas |

## Produtos

Prefixo: `/api/v1/products`

| Método | Caminho | Autenticação | Descrição |
| --- | --- | --- | --- |
| `POST` | `/` | Sim | Cria produto |
| `GET` | `/` | Sim | Lista produtos |
| `GET` | `/{product_id}` | Sim | Busca produto por ID e valida proprietário |
| `PUT` | `/{product_id}` | Sim | Atualiza produto e valida proprietário |
| `DELETE` | `/{product_id}` | Sim | Remove produto e valida proprietário |

### Campos de Criação

```json
{
  "name": "Corolla XEI",
  "description": "Sedan automático",
  "price": "145000.00",
  "stock": 3,
  "status": "in_stock",
  "condition": "used",
  "is_available": true,
  "brand_id": 1,
  "seller_id": 1
}
```

### Enums

| Campo | Valores |
| --- | --- |
| `status` | `in_stock`, `out_of_stock` |
| `condition` | `new`, `used`, `refurbished` |

### Query Parameters de Listagem

| Parâmetro | Tipo | Descrição |
| --- | --- | --- |
| `offset` | `int` | Quantidade de registros ignorados |
| `limit` | `int` | Quantidade máxima de registros, entre `1` e `100` |
| `search` | `string` | Busca por nome |
| `brand_id` | `int` | Filtra por marca |
| `seller_id` | `int` | Filtra por vendedor |
| `condition` | `enum` | Filtra por condição |
| `status` | `enum` | Filtra por status |
| `is_available` | `bool` | Filtra por disponibilidade |
| `min_price` | `float` | Preço mínimo |
| `max_price` | `float` | Preço máximo |

