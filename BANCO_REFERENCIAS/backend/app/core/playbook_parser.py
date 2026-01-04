"""
Parser de templates de playbooks.
"""
import re
from typing import Dict, Any, List


class PlaybookParser:
    """Parser para templates de playbooks com variáveis."""
    
    # Padrão para variáveis: {{variable_name}}
    VARIABLE_PATTERN = r'\{\{(\w+)\}\}'
    
    @classmethod
    def extract_variables(cls, template: str) -> List[str]:
        """
        Extrai lista de variáveis do template.
        
        Args:
            template: Template Markdown com variáveis
            
        Returns:
            Lista de nomes de variáveis
        """
        matches = re.findall(cls.VARIABLE_PATTERN, template)
        return list(set(matches))  # Remove duplicatas
    
    @classmethod
    def render(cls, template: str, variables: Dict[str, Any]) -> str:
        """
        Renderiza template substituindo variáveis.
        
        Args:
            template: Template Markdown com variáveis
            variables: Dicionário com valores das variáveis
            
        Returns:
            Template renderizado
            
        Raises:
            ValueError: Se variável obrigatória não fornecida
        """
        # Extrai variáveis do template
        required_vars = cls.extract_variables(template)
        
        # Verifica se todas as variáveis foram fornecidas
        missing_vars = [var for var in required_vars if var not in variables]
        if missing_vars:
            raise ValueError(f"Variáveis obrigatórias não fornecidas: {', '.join(missing_vars)}")
        
        # Renderiza template
        rendered = template
        for var_name, var_value in variables.items():
            placeholder = f"{{{{{var_name}}}}}"
            rendered = rendered.replace(placeholder, str(var_value))
        
        return rendered
    
    @classmethod
    def validate_template(cls, template: str) -> bool:
        """
        Valida formato do template.
        
        Args:
            template: Template para validar
            
        Returns:
            True se válido
        """
        # Verifica se template não está vazio
        if not template or not template.strip():
            return False
        
        # Verifica se todas as chaves {{ estão fechadas
        open_count = template.count('{{')
        close_count = template.count('}}')
        if open_count != close_count:
            return False
        
        # Verifica formato das variáveis
        matches = re.findall(cls.VARIABLE_PATTERN, template)
        # Se tem {{ mas não encontrou matches, formato está errado
        if open_count > 0 and len(matches) == 0:
            return False
        
        return True

