# FastAPI_auth
Um serviço de autenticação RESTful completo construído com FastAPI, JWT e SQLAlchemy.

![Python](https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-green?style=for-the-badge&logo=fastapi)
![Status](https://img.shields.io/badge/Status-Funcional-brightgreen?style=for-the-badge)

Um serviço de autenticação RESTful completo e robusto, desenvolvido com as melhores práticas usando FastAPI. Este projeto serve como uma base sólida e um ponto de partida para qualquer aplicação que necessite de gerenciamento de usuários, incluindo cadastro seguro, login com tokens JWT e proteção de rotas.

## ✨ Principais Funcionalidades

-   ✅ **Cadastro de Usuários:** Endpoint seguro para registrar novos usuários com validação de dados e prevenção de emails duplicados.
-   🔒 **Segurança de Senhas:** As senhas são seguramente "hasheadas" usando o algoritmo **bcrypt** e nunca são armazenadas em texto puro.
-   🔑 **Autenticação via JWT:** Geração de JSON Web Tokens (JWT) assinados com tempo de expiração para autenticar os usuários após o login.
-   🛡️ **Rotas Protegidas:** Exemplo de endpoint (`/users/me`) que só pode ser acessado por usuários autenticados com um token JWT válido.
-   📖 **Documentação Automática:** Interfaces interativas do Swagger UI (`/docs`) e ReDoc (`/redoc`) geradas automaticamente pelo FastAPI para fácil visualização e teste dos endpoints.

## 🛠️ Tecnologias Utilizadas

-   **Backend:** Python 3.11+
-   **Framework:** FastAPI
-   **Validação de Dados:** Pydantic
-   **Banco de Dados (ORM):** SQLAlchemy com SQLite
-   **Segurança:** Passlib (para hashing de senhas), python-jose (para JWT)
-   **Servidor ASGI:** Uvicorn

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar e rodar o projeto em seu ambiente local.

### 1. Pré-requisitos
-   Python 3.11 ou superior
-   Git

### 2. Clone o repositório
```bash
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
cd seu-repositorio
```


### 3. Crie e ative o ambiente virtual

# Para Windows
python -m venv venv
.\venv\Scripts\activate

# Para Linux/macOS
python3 -m venv venv
source venv/bin/activate

### 4. Instale as dependencias

pip install -r requirements.txt

### 5. Configure as Variáveis de Ambiente

# .env
DATABASE_URL="sqlite:///./test.db"

# Para gerar uma chave segura, use o comando: openssl rand -hex 32
SECRET_KEY="<sua_chave_secreta_super_segura_aqui>"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

### 6. Inicie o servidor

uvicorn app.main:app --reload


🌐 Endpoints da API
Acesse http://127.0.0.1:8000/docs para uma documentação interativa completa.

Método	Endpoint	Descrição	Acesso
POST	/auth/register	Registra um novo usuário.	Público
POST	/auth/token	Autentica um usuário e retorna um token.	Público
GET	/auth/users/me	Retorna os dados do usuário logado.	Protegido
📝 Possíveis Melhorias (To-Do)
[ ] Implementar fluxo de "Esqueci minha senha" com envio de email.

[ ] Adicionar testes automatizados com pytest.

[ ] Implementar um sistema de "refresh tokens".

[ ] Adicionar um sistema de roles e permissões para usuários (ex: admin, user).
