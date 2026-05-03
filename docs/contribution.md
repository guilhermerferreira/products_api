# Contribuição

## Fluxo de Trabalho

1. Criar uma branch a partir da branch principal.
2. Implementar a alteração de forma pequena e revisável.
3. Atualizar ou adicionar testes.
4. Rodar lint, formatação e testes.
5. Atualizar documentação quando houver mudança de comportamento ou contrato.
6. Abrir pull request com descrição objetiva.

## Padrões de Commit

Use mensagens claras e no imperativo quando possível:

```text
Add product ownership validation
Fix user password update
Update API endpoint docs
```

## Critérios para Pull Request

- Alteração tem escopo claro.
- Não inclui segredos.
- Não inclui arquivos gerados desnecessários.
- Endpoints novos possuem schemas de entrada e saída.
- Alterações de banco possuem migration Alembic.
- Comportamento protegido possui validação de autenticação e autorização.

## Revisão

Durante a revisão, priorize:

- Correção das regras de negócio.
- Segurança de autenticação e autorização.
- Consistência dos contratos Pydantic.
- Integridade das relações SQLAlchemy.
- Impacto em migrações.
- Cobertura de testes para fluxos críticos.

