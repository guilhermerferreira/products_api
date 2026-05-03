# Deploy

## Preparação

Antes do deploy:

- Definir variáveis de ambiente reais.
- Usar `JWT_SECRET_KEY` forte.
- Configurar banco de dados persistente.
- Executar migrações.
- Validar health check.
- Rodar lint e testes disponíveis.

## Variáveis de Ambiente

Exemplo:

```env
DATABASE_URL=postgresql+asyncpg://usuario:senha@host:5432/products_api
JWT_SECRET_KEY=segredo-forte
JWT_ALGORITHM=HS256
JWT_EXPIRATION_MINUTES=30
```

## Migrações no Deploy

Execute antes de subir ou liberar tráfego para a nova versão:

```bash
poetry run alembic upgrade head
```

## Servidor ASGI

Em produção, use um servidor ASGI apropriado. Exemplo com Uvicorn:

```bash
poetry run uvicorn products_api.app:app --host 0.0.0.0 --port 8000
```

Também é possível usar Gunicorn com worker Uvicorn, se estiver disponível no ambiente:

```bash
gunicorn products_api.app:app -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000
```

## Health Check

Endpoint:

```http
GET /
```

Resposta esperada:

```json
{
  "status": "ok"
}
```

## Checklist

- Banco acessível pela aplicação.
- Migrations aplicadas.
- Segredos configurados fora do código.
- Logs habilitados no ambiente de execução.
- HTTPS configurado no proxy ou plataforma.
- Swagger/ReDoc avaliados conforme política do ambiente.

