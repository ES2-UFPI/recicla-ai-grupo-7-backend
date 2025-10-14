<h1 align="center">RECICLA AÍ BACKEND</h1>
Repositório do backend do projeto Recicla Aí, uma plataforma dedicada a promover a reciclagem e a sustentabilidade ambiental.

# 🐳 Executando com Docker (Recomendado)

## Pré-requisitos
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado e em execução
- [Git](https://git-scm.com/) instalado

## Desenvolvimento Local (com PostgreSQL)

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/ES2-UFPI/recicla-ai-grupo-7-backend.git
   cd recicla-ai-grupo-7-backend
   ```

2. **Configure as variáveis de ambiente**:
   ```bash
   # Windows
   Copy-Item .env.example .env
   
   # Linux/Mac
   cp .env.example .env
   ```

3. **Inicie os containers**:
   ```bash
   docker compose -f docker-compose-local.yml up --build
   ```

4. **Acesse a aplicação**:
   - Backend: http://localhost:5000
   - Banco de dados: `localhost:5432`

5. **Parar os containers**:
   ```bash
   docker compose -f docker-compose-local.yml down
   ```

6. **Limpar banco de dados** (remove volumes):
   ```bash
   docker compose -f docker-compose-local.yml down -v
   ```

## Produção (sem PostgreSQL local)

Para executar apenas o backend em produção (conectando a um banco externo):

1. **Configure o arquivo `.env`** com a URL do banco de produção:
   ```env
   DATABASE_URL=postgresql://usuario:senha@host-producao:5432/recicla_ai
   ```

2. **Execute**:
   ```bash
   docker compose -f docker-compose.yml up --build
   ```

# 📊 Gerenciamento do Banco de Dados

## Acessar o PostgreSQL via CLI

```bash
# Entrar no container
docker exec -it recicla-ai-db psql -U postgres -d recicla_ai

# Comandos úteis dentro do psql:
\dt              # Listar todas as tabelas
\d nome_tabela   # Ver estrutura de uma tabela
\l               # Listar databases
\q               # Sair
```

## Executar queries direto do terminal

```bash
# Listar tabelas
docker exec -it recicla-ai-db psql -U postgres -d recicla_ai -c "\dt"

# Ver dados de uma tabela
docker exec -it recicla-ai-db psql -U postgres -d recicla_ai -c "SELECT * FROM users;"
```

## Ferramentas Gráficas (GUI)

Você pode conectar ferramentas como **DBeaver** ou **pgAdmin** com as seguintes credenciais:
- **Host**: `localhost`
- **Port**: `5432`
- **Database**: `recicla_ai`
- **Username**: `postgres`
- **Password**: `postgres`

# 🔧 SQLC - Geração de Código

O projeto utiliza [sqlc](https://sqlc.dev/) para gerar código Python type-safe a partir de queries SQL.

## Gerando código SQLC localmente

1. **Instale o sqlc**:
   - Linux/Mac: https://docs.sqlc.dev/en/latest/overview/install.html
   - Windows: Baixe o binário do [GitHub Releases](https://github.com/sqlc-dev/sqlc/releases)

2. **Gere os arquivos**:
   ```bash
   sqlc generate
   ```

Os arquivos gerados estarão em `sql/generated/`.

**Nota**: No Docker, os arquivos são gerados automaticamente durante o build.

# 💻 Executando Localmente (sem Docker)

## Preparando a Virtual Environment

Para garantir que todas as dependências do projeto sejam gerenciadas corretamente, é recomendado o uso de uma virtual environment. Siga os passos abaixo para configurar a sua:

1. **Criar a Virtual Environment**:
   ```bash
   python -m venv venv
   ```
   - Em algumas versões do linux é necessário atualizar a versão do venv, como no caso do python 3.12 no ubuntu 24.04:
   ```bash
   sudo apt install python3.12-venv -y
   ```

2. **Ativar a Virtual Environment**:
    - No Windows:
        ```bash
        venv\Scripts\activate
        ```
    - No macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

3. **Instalar as Dependências**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure o PostgreSQL local** e atualize a `DATABASE_URL` no arquivo `.env`:
   ```env
   DATABASE_URL=postgresql://postgres:postgres@localhost:5432/recicla_ai
   ```

5. **Execute o projeto**:
   ```bash
   python main.py
   ```

# 📦 Requirements

As dependências do projeto estão listadas no arquivo `requirements.txt`. Certifique-se de instalar todas as dependências usando o comando mencionado acima.

## Como construir o arquivo requirements.txt

Para gerar o arquivo `requirements.txt` com as dependências atuais do seu ambiente virtual, utilize o seguinte comando:
```bash
pip freeze > requirements.txt
```

## Como instalar as dependências do requirements.txt

Para instalar todas as dependências listadas no arquivo `requirements.txt`, utilize o comando:
```bash
pip install -r requirements.txt
```

# 🗂️ Estrutura do Projeto

```
recicla-ai-grupo-7-backend/
├── src/
│   ├── api/           # Rotas e endpoints
│   ├── database/      # Configuração de conexão
│   ├── middlewares/   # Middlewares do Flask
│   ├── models/        # Modelos de dados
│   └── utils/         # Utilitários
├── sql/
│   ├── schema.sql     # Schema do banco de dados
│   ├── queries.sql    # Queries SQL para SQLC
│   └── generated/     # Código Python gerado pelo SQLC (não commitar)
├── scripts/           # Scripts auxiliares
├── main.py            # Ponto de entrada da aplicação
├── requirements.txt   # Dependências Python
├── Dockerfile         # Configuração Docker
├── docker-compose-local.yml      # Docker Compose para desenvolvimento
├── docker-compose.yml            # Docker Compose para produção
├── sqlc.yaml          # Configuração do SQLC
└── README.md          # Este arquivo
```

# 🚀 Deploy em Produção

Para deploy em servidores Linux (sem Docker Desktop):

1. **Instale Docker Engine**:
   ```bash
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   ```

2. **Clone e configure o projeto**:
   ```bash
   git clone https://github.com/ES2-UFPI/recicla-ai-grupo-7-backend.git
   cd recicla-ai-grupo-7-backend
   nano .env  # Configure DATABASE_URL
   ```

3. **Execute**:
   ```bash
   docker compose -f docker-compose.yml up -d
   ```

4. **Ver logs**:
   ```bash
   docker compose -f docker-compose.yml logs -f
   ```