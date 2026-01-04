"""
Validadores para operações da aplicação.
"""
from typing import Optional
from app.core.config import settings
from app.core.exceptions import FileTooLargeError, InvalidFileTypeError, InvalidQueryError


def validate_file_size(file_size_bytes: int) -> None:
    """
    Valida tamanho do arquivo.
    
    Args:
        file_size_bytes: Tamanho do arquivo em bytes
        
    Raises:
        FileTooLargeError: Se arquivo exceder tamanho máximo
    """
    if file_size_bytes > settings.MAX_FILE_SIZE_BYTES:
        raise FileTooLargeError(file_size_bytes, settings.MAX_FILE_SIZE_BYTES)


def validate_file_type(mime_type: Optional[str], filename: Optional[str] = None) -> None:
    """
    Valida tipo de arquivo.
    
    Args:
        mime_type: Tipo MIME do arquivo
        filename: Nome do arquivo (opcional, usado para inferir tipo se mime_type não fornecido)
        
    Raises:
        InvalidFileTypeError: Se tipo de arquivo não for permitido
    """
    # Se não tem mime_type e não tem filename, não pode validar
    if not mime_type and not filename:
        raise InvalidFileTypeError("unknown", settings.ALLOWED_FILE_TYPES)
    
    # Se mime_type fornecido, valida diretamente
    if mime_type:
        if mime_type not in settings.ALLOWED_FILE_TYPES:
            raise InvalidFileTypeError(mime_type, settings.ALLOWED_FILE_TYPES)
        return
    
    # Se só tem filename, tenta inferir tipo pela extensão
    if filename:
        extension = filename.lower().split('.')[-1] if '.' in filename else ''
        extension_to_mime = {
            'pdf': 'application/pdf',
            'docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            'doc': 'application/msword',
            'txt': 'text/plain',
            'md': 'text/markdown',
            'json': 'application/json',
        }
        
        inferred_mime = extension_to_mime.get(extension)
        if inferred_mime:
            # Valida o tipo inferido
            if inferred_mime not in settings.ALLOWED_FILE_TYPES:
                raise InvalidFileTypeError(f"inferred: {inferred_mime} (from .{extension})", settings.ALLOWED_FILE_TYPES)
        else:
            # Extensão não reconhecida
            raise InvalidFileTypeError(f"unknown extension: .{extension}", settings.ALLOWED_FILE_TYPES)


def validate_search_query(query: str) -> None:
    """
    Valida query de busca.
    
    Args:
        query: Query de busca
        
    Raises:
        InvalidQueryError: Se query for inválida
    """
    if not query or not query.strip():
        raise InvalidQueryError("Query não pode estar vazia")
    
    query = query.strip()
    
    if len(query) < settings.MIN_QUERY_LENGTH:
        raise InvalidQueryError(
            f"Query muito curta (mínimo {settings.MIN_QUERY_LENGTH} caracteres)"
        )
    
    if len(query) > settings.MAX_QUERY_LENGTH:
        raise InvalidQueryError(
            f"Query muito longa (máximo {settings.MAX_QUERY_LENGTH} caracteres)"
        )

