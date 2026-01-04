"""
Métricas Prometheus para monitoramento.
"""
from prometheus_client import Counter, Histogram, Gauge
from typing import Optional
import time

# Counters
document_uploads_total = Counter(
    'document_uploads_total',
    'Total number of document uploads',
    ['status']  # success, error
)

document_deletes_total = Counter(
    'document_deletes_total',
    'Total number of document deletes',
    ['status']
)

search_requests_total = Counter(
    'search_requests_total',
    'Total number of search requests',
    ['status', 'cached']  # cached: true, false
)

api_requests_total = Counter(
    'api_requests_total',
    'Total number of API requests',
    ['method', 'endpoint', 'status_code']
)

# Histograms
document_upload_duration = Histogram(
    'document_upload_duration_seconds',
    'Time spent uploading documents',
    buckets=[0.1, 0.5, 1.0, 2.5, 5.0, 10.0]
)

search_duration = Histogram(
    'search_duration_seconds',
    'Time spent on search requests',
    buckets=[0.1, 0.5, 1.0, 2.5, 5.0, 10.0, 30.0]
)

api_request_duration = Histogram(
    'api_request_duration_seconds',
    'Time spent processing API requests',
    ['method', 'endpoint'],
    buckets=[0.01, 0.05, 0.1, 0.5, 1.0, 2.5, 5.0]
)

# Gauges
active_documents = Gauge(
    'active_documents_total',
    'Total number of active documents'
)

cache_size = Gauge(
    'cache_size_bytes',
    'Size of cache in bytes'
)


class MetricsMiddleware:
    """Middleware para coletar métricas de requisições."""
    
    def __init__(self, app):
        self.app = app
    
    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return
        
        method = scope["method"]
        path = scope["path"]
        start_time = time.time()
        
        # Normalizar path para métricas (remover IDs)
        endpoint = self._normalize_path(path)
        
        async def send_wrapper(message):
            if message["type"] == "http.response.start":
                status_code = message["status"]
                api_requests_total.labels(
                    method=method,
                    endpoint=endpoint,
                    status_code=status_code
                ).inc()
                
                duration = time.time() - start_time
                api_request_duration.labels(
                    method=method,
                    endpoint=endpoint
                ).observe(duration)
            
            await send(message)
        
        await self.app(scope, receive, send_wrapper)
    
    def _normalize_path(self, path: str) -> str:
        """Normaliza path removendo IDs UUID."""
        import re
        # Substitui UUIDs por {id}
        path = re.sub(
            r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}',
            '{id}',
            path,
            flags=re.IGNORECASE
        )
        return path


def record_document_upload(success: bool, duration: float):
    """Registra métrica de upload de documento."""
    status = 'success' if success else 'error'
    document_uploads_total.labels(status=status).inc()
    if success:
        document_upload_duration.observe(duration)


def record_document_delete(success: bool):
    """Registra métrica de deleção de documento."""
    status = 'success' if success else 'error'
    document_deletes_total.labels(status=status).inc()


def record_search(cached: bool, duration: float, success: bool = True):
    """Registra métrica de busca."""
    status = 'success' if success else 'error'
    cached_str = 'true' if cached else 'false'
    search_requests_total.labels(status=status, cached=cached_str).inc()
    if success:
        search_duration.observe(duration)


def update_active_documents(count: int):
    """Atualiza gauge de documentos ativos."""
    active_documents.set(count)

