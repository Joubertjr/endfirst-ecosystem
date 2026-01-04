### 5.4 Estratégia de Testes (v2.1)

| Tipo de Teste | Ferramenta | Cobertura Mínima | Fase |
|---|---|---|---|
| **Unit Tests** | pytest | 80% | MVP |
| **Integration Tests** | pytest + httpx | Endpoints críticos | MVP |
| **E2E Tests** | Playwright | Fluxos principais | Beta |
| **Load Tests** | k6 / Locust | 1.000 req/s | Produção |
