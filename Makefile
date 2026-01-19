.PHONY: help z12 z12-audit z12-docs clean

# Default target
help:
	@echo "========================================="
	@echo "END-FIRST Ecosystem - Makefile"
	@echo "========================================="
	@echo ""
	@echo "Targets disponíveis:"
	@echo "  make z12        - Executa Gate Z12 completo (Z12-A + Z12-B)"
	@echo "  make z12-audit  - Executa apenas Z12-A (Auditoria de Método)"
	@echo "  make z12-docs   - Executa apenas Z12-B (Auditoria de Documentação)"
	@echo "  make help       - Mostra esta mensagem de ajuda"
	@echo ""

# Gate Z12 completo (Z12-A + Z12-B)
z12: z12-audit z12-docs
	@echo ""
	@echo "========================================="
	@echo "Gate Z12 — PASS"
	@echo "========================================="
	@echo ""
	@echo "Todas as validações passaram."
	@echo "Você pode prosseguir para declarar DONE."
	@echo ""

# Z12-A: Auditoria de Método
z12-audit:
	@echo ""
	@./tools/z12_audit.sh

# Z12-B: Auditoria de Documentação
z12-docs:
	@echo ""
	@./tools/z12_docs_check.sh

# Clean (placeholder para futuras necessidades)
clean:
	@echo "Nada para limpar no momento."
