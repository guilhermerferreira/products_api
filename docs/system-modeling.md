# Modelagem do Sistema

## Modelos de Dados

```mermaid
erDiagram
    USERS ||--o{ PRODUCTS : vende
    BRANDS ||--o{ PRODUCTS : classifica

    USERS {
        int id PK
        string username UK
        string email UK
        string password
        datetime created_at
        datetime updated_at
    }

    BRANDS {
        int id PK
        string name UK
        boolean is_active
        text description
        datetime created_at
        datetime updated_at
    }

    PRODUCTS {
        int id PK
        string name UK
        text description
        decimal price
        int stock
        enum status
        enum condition
        boolean is_available
        int brand_id FK
        int seller_id FK
        datetime created_at
        datetime updated_at
    }
```

## Arquitetura do Sistema

```mermaid
flowchart TD
    Client[Cliente HTTP] --> FastAPI[FastAPI App]
    FastAPI --> Routers[Routers]
    Routers --> Schemas[Schemas Pydantic]
    Routers --> Security[Seguranca JWT e Hash]
    Routers --> Session[AsyncSession]
    Session --> Models[Modelos SQLAlchemy]
    Models --> DB[(Banco de Dados)]
    Alembic[Alembic] --> DB
    Settings[Settings .env] --> FastAPI
    Settings --> Session
    Settings --> Alembic
```

## Fluxo de Autenticação

```mermaid
sequenceDiagram
    actor Client as Cliente
    participant API as FastAPI
    participant Auth as Auth Router
    participant Security as Security
    participant DB as Banco de Dados

    Client->>API: POST /api/v1/auth/token
    API->>Auth: LoginRequest
    Auth->>DB: Buscar usuario por email
    DB-->>Auth: Usuario
    Auth->>Security: Verificar senha
    Security-->>Auth: Senha valida
    Auth->>Security: Criar JWT com sub=user.id
    Security-->>Auth: access_token
    Auth-->>Client: Token bearer
```

## Fluxo CRUD de Carros

No código atual, o recurso implementado é `Product`. Para o domínio de carros, cada produto pode representar um carro.

```mermaid
flowchart TD
    Start[Cliente autenticado] --> Action{Operacao}
    Action --> Create[Criar carro/produto]
    Action --> List[Listar carros/produtos]
    Action --> Read[Buscar por ID]
    Action --> Update[Atualizar]
    Action --> Delete[Remover]

    Create --> ValidateCreate[Validar nome, preco, estoque, marca e vendedor]
    ValidateCreate --> SaveCreate[Salvar no banco]
    SaveCreate --> ReturnCreate[Retornar 201]

    List --> ApplyFilters[Aplicar filtros e paginacao]
    ApplyFilters --> ReturnList[Retornar lista]

    Read --> LoadRead[Carregar produto com marca e vendedor]
    LoadRead --> CheckOwnerRead[Validar vendedor proprietario]
    CheckOwnerRead --> ReturnRead[Retornar produto]

    Update --> LoadUpdate[Carregar produto]
    LoadUpdate --> CheckOwnerUpdate[Validar vendedor proprietario]
    CheckOwnerUpdate --> ValidateUpdate[Validar campos alterados]
    ValidateUpdate --> SaveUpdate[Salvar alteracoes]
    SaveUpdate --> ReturnUpdate[Retornar produto atualizado]

    Delete --> LoadDelete[Carregar produto]
    LoadDelete --> CheckOwnerDelete[Validar vendedor proprietario]
    CheckOwnerDelete --> Remove[Excluir do banco]
    Remove --> ReturnDelete[Retornar 204]
```

## Fluxo de Segurança

```mermaid
flowchart TD
    Request[Requisicao protegida] --> Header{Tem Authorization Bearer?}
    Header -- Nao --> Unauthorized[401 Unauthorized]
    Header -- Sim --> Decode[Decodificar JWT]
    Decode --> Valid{Token valido e nao expirado?}
    Valid -- Nao --> Unauthorized
    Valid -- Sim --> Subject{Payload tem sub?}
    Subject -- Nao --> Unauthorized
    Subject -- Sim --> LoadUser[Buscar usuario pelo sub]
    LoadUser --> UserFound{Usuario existe?}
    UserFound -- Nao --> Unauthorized
    UserFound -- Sim --> Protected[Executar endpoint]
    Protected --> Ownership{Endpoint exige ownership?}
    Ownership -- Nao --> Response[Retornar resposta]
    Ownership -- Sim --> Compare{current_user.id igual seller_id?}
    Compare -- Sim --> Response
    Compare -- Nao --> Forbidden[403 Forbidden]
```

