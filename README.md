# 📮 CEP Finder

Aplicação web para consultar endereços pelo CEP, com histórico salvo em banco de dados.

## Tecnologias

- Python 3.14
- FastAPI
- PostgreSQL
- Jinja2 (templates HTML)
- API ViaCEP

## Como rodar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/jvieira11/cep-finder.git
cd cep-finder
```

### 2. Instale as dependências

```bash
pip install fastapi uvicorn psycopg2-binary requests jinja2 python-dotenv aiofiles python-multipart
```

### 3. Configure o banco de dados

Crie um banco PostgreSQL chamado `ceps_db` e execute:

```sql
CREATE TABLE consultas_cep (
    id            SERIAL PRIMARY KEY,
    cep           VARCHAR(9),
    logradouro    VARCHAR(200),
    bairro        VARCHAR(100),
    cidade        VARCHAR(100),
    estado        VARCHAR(2),
    consultado_em TIMESTAMP DEFAULT NOW()
);
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```
DB_HOST=localhost
DB_NAME=ceps_db
DB_USER=postgres
DB_PASSWORD=sua_senha
DB_PORT=5432
```

### 5. Rode o servidor

```bash
python -m uvicorn app:app --reload
```

Acesse em **http://localhost:8000**

## Funcionalidades

- Busca de endereço por CEP via API ViaCEP
- Salvamento automático no banco de dados
- Histórico completo de consultas