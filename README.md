

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
