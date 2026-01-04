### 4.2 Modelo de Dados (v2.1)

#### Tabela `documents` (Atualizada)
```sql
CREATE TABLE documents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    project_id UUID REFERENCES projects(id) ON DELETE CASCADE,
    google_file_id VARCHAR(255) UNIQUE NOT NULL,
    backup_storage_url TEXT, -- NOVO (RNF-07)
    filename VARCHAR(500) NOT NULL,
    file_type VARCHAR(50),
    file_size_bytes BIGINT,
    version INT DEFAULT 1, -- NOVO (RF-11)
    status VARCHAR(50) DEFAULT 'draft', -- NOVO (RF-11)
    tags TEXT[], -- NOVO (RF-08)
    category VARCHAR(100), -- NOVO (RF-08)
    custom_metadata JSONB, -- NOVO (RF-08)
    upload_date TIMESTAMP DEFAULT NOW(),
    metadata JSONB,
    INDEX idx_user_id (user_id),
    INDEX idx_project_id (project_id),
    INDEX idx_google_file_id (google_file_id),
    INDEX idx_tags ON documents USING GIN(tags),
    INDEX idx_category ON documents(category)
);
```

#### Tabela `analysis_feedback` (Nova)
```sql
CREATE TABLE analysis_feedback (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    analysis_id UUID REFERENCES analyses(id) ON DELETE CASCADE,
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    feedback_text TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
```

#### Tabela `cost_tracking` (Nova)
```sql
CREATE TABLE cost_tracking (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    date DATE,
    service VARCHAR(50), -- 'file_search', 'gemini', 'storage'
    tokens_used BIGINT,
    estimated_cost_usd DECIMAL(10,2),
    created_at TIMESTAMP
);
```
