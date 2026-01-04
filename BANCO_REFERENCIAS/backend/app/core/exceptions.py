"""
Exceções customizadas da aplicação.
"""
from fastapi import HTTPException, status


class BancoReferenciasException(HTTPException):
    """Exceção base da aplicação."""
    pass


class DocumentNotFoundError(BancoReferenciasException):
    """Documento não encontrado."""
    def __init__(self, document_id: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Documento '{document_id}' não encontrado"
        )


class ReferenceNotFoundError(BancoReferenciasException):
    """Referência não encontrada."""
    def __init__(self, reference_id: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Referência '{reference_id}' não encontrada"
        )


class ProjectNotFoundError(BancoReferenciasException):
    """Projeto não encontrado."""
    def __init__(self, project_id: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Projeto '{project_id}' não encontrado"
        )


class GoogleFileSearchError(BancoReferenciasException):
    """Erro ao interagir com Google File Search."""
    def __init__(self, message: str):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro no Google File Search: {message}"
        )


class AuthenticationError(Exception):
    """Erro de autenticação."""
    pass


class ValidationError(BancoReferenciasException):
    """Erro de validação."""
    def __init__(self, message: str):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Erro de validação: {message}"
        )


class FileTooLargeError(ValidationError):
    """Arquivo muito grande."""
    def __init__(self, file_size: int, max_size: int):
        super().__init__(
            f"Arquivo muito grande ({file_size / (1024*1024):.2f} MB). "
            f"Tamanho máximo permitido: {max_size / (1024*1024):.2f} MB"
        )


class InvalidFileTypeError(ValidationError):
    """Tipo de arquivo não permitido."""
    def __init__(self, file_type: str, allowed_types: list[str]):
        super().__init__(
            f"Tipo de arquivo '{file_type}' não permitido. "
            f"Tipos permitidos: {', '.join(allowed_types)}"
        )


class InvalidQueryError(ValidationError):
    """Query de busca inválida."""
    def __init__(self, message: str):
        super().__init__(f"Query de busca inválida: {message}")


class PlaybookNotFoundError(BancoReferenciasException):
    """Playbook não encontrado."""
    def __init__(self, playbook_id: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Playbook '{playbook_id}' não encontrado"
        )


class AnalysisNotFoundError(BancoReferenciasException):
    """Análise não encontrada."""
    def __init__(self, analysis_id: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Análise '{analysis_id}' não encontrada"
        )

