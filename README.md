

1. Criar e ativar o ambiente virtual
bash

python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell
.venv\Scripts\Activate.ps1

2. Instalar o Poetry dentro do venv
bash

pip install poetry

3. Inicializar o projeto com Poetry (sem interação)
bash

poetry init --no-interaction \
  --name bank-api \
  --description "API bancária assíncrona com FastAPI, JWT e banco in-memory" \
  --author "Seu Nome <seuemail@example.com>" \
  --dependency fastapi \
  --dependency "uvicorn[standard]" \
  --dependency python-multipart \
  --dependency pydantic \
  --dependency "passlib[bcrypt]" \
  --dependency PyJWT

4. Instalar dependências
bash

poetry install

5. Rodar o servidor FastAPI
bash

poetry run uvicorn app.main:app --reload

6. Acessar a API

    API: http://127.0.0.1:8000

    Documentação Swagger: http://127.0.0.1:8000/docs



markdown

# 📘 API Bancária Assíncrona

## 🏗️ Visão Geral
Esta API foi desenvolvida com **FastAPI** e fornece operações básicas de um sistema bancário:

- Cadastro e autenticação de usuários com **JWT**.
- Criação e listagem de contas correntes.
- (Previsto) Depósitos, saques e extratos.

A documentação interativa está disponível em:
- **Swagger UI:** `/docs`
- **Redoc:** `/redoc`

---

## ⚙️ Configuração
```python
app = FastAPI(
    title="API Bancária Assíncrona",
    description="API para depósitos, saques e extrato de contas correntes com JWT e FastAPI.",
    version="1.0.0",
)

Define título, descrição e versão da API, exibidos automaticamente na documentação.
🔑 Autenticação (/auth)
1. Cadastro de Usuário

Endpoint: POST /auth/signup  
Tags: Auth
Request Body (UserCreate)
json

{
  "username": "joao",
  "password": "senha123"
}

Response (User)
json

{
  "id": 1,
  "username": "joao"
}

Possíveis Erros

    400 Bad Request → Usuário já existe.

Exemplos
bash

# Usando curl
curl -X POST http://localhost:8000/auth/signup \
  -H "Content-Type: application/json" \
  -d '{"username":"joao","password":"senha123"}'

# Usando httpie
http POST http://localhost:8000/auth/signup username=joao password=senha123

2. Login e Token JWT

Endpoint: POST /auth/token  
Tags: Auth
Request (form-data)
Código

username=joao
password=senha123

Response (Token)
json

{
  "access_token": "jwt-gerado-aqui"
}

Possíveis Erros

    401 Unauthorized → Credenciais inválidas.

Observação

O token deve ser enviado em chamadas autenticadas no header:
Código

Authorization: Bearer <token>

Exemplos
bash

# Usando curl
curl -X POST http://localhost:8000/auth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=joao&password=senha123"

# Usando httpie
http -f POST http://localhost:8000/auth/token username=joao password=senha123

💳 Contas (/accounts)
3. Criar Conta

Endpoint: POST /accounts  
Tags: Contas
Request Body (AccountCreate)
json

{
  "name": "Conta Corrente Principal"
}

Response (Account)
json

{
  "id": 1,
  "user_id": 1,
  "name": "Conta Corrente Principal",
  "balance": 0.0
}

Possíveis Erros

    401 Unauthorized → Token não fornecido ou inválido.

Exemplos
bash

# Usando curl
curl -X POST http://localhost:8000/accounts \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"name":"Conta Corrente Principal"}'

# Usando httpie
http POST http://localhost:8000/accounts \
  name="Conta Corrente Principal" \
  "Authorization:Bearer <token>"

4. Listar Contas

Endpoint: GET /accounts  
Tags: Contas
Response (List[Account])
json

[
  {
    "id": 1,
    "user_id": 1,
    "name": "Conta Corrente Principal",
    "balance": 0.0
  },
  {
    "id": 2,
    "user_id": 1,
    "name": "Conta Poupança",
    "balance": 1500.0
  }
]

Possíveis Erros

    401 Unauthorized → Token não fornecido ou inválido.

Exemplos
bash

# Usando curl
curl -X GET http://localhost:8000/accounts \
  -H "Authorization: Bearer <token>"

# Usando httpie
http GET http://localhost:8000/accounts "Authorization:Bearer <token>"

🛠️ Utilitários

    hash_password / verify_password → Proteção de senhas.

    create_access_token → Geração de JWT.

    get_current_user → Valida token e retorna usuário logado.

    db → Camada de acesso ao banco de dados.

    Schemas (User, Account, etc.) → Estrutura dos dados de entrada/saída.

📌 Funcionalidades Futuras

Pelos imports, estão previstos:

    Transações (TransactionCreate, Transaction) → Depósitos e saques.

    Extrato (Statement) → Histórico de movimentações.

🚀 Exemplo de Fluxo

    Cadastrar usuário → POST /auth/signup

    Login → POST /auth/token → recebe JWT

    Criar conta → POST /accounts (com JWT no header)

    Listar contas → GET /accounts (com JWT no header)

⚠️ Códigos de Erro Documentados
Código	Significado	Onde pode ocorrer
400	Usuário já existe	/auth/signup
401	Credenciais inválidas ou token ausente	/auth/token, /accounts
403	Acesso negado	Endpoints futuros com regras de permissão
404	Recurso não encontrado	Endpoints futuros (conta inexistente, transação inexistente)
📄 Licença

Este projeto é apenas um exemplo educacional, de um projeto de estudos na Dio.me
Código


