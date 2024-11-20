# Enjoei2025 - Sistema de Cadastro e Pagamento

Este projeto é um sistema de cadastro e pagamento para a plataforma Enjoei, com um backend em Python Flask e um frontend em PHP.

## Requisitos

### Backend (Python Flask):
- Python 3.8+
- MySQL 8.0+
- pip (gerenciador de pacotes do Python)

### Frontend (PHP):
- PHP 7.4 ou superior
- MySQL 5.7 ou superior
- Servidor web (Apache ou Nginx)

## Instalação e Configuração

### Backend (Python Flask):

1. Clone o repositório:
   ```
   git clone https://github.com/iraci2024/enjoei2025.git
   cd enjoei2025
   ```

2. Crie um ambiente virtual e ative-o:
   ```
   python -m venv venv
   venv\Scripts\activate  # No Windows
   source venv/bin/activate  # No macOS/Linux
   ```

3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente:
   - Crie um arquivo `.env` na raiz do projeto
   - Adicione as seguintes variáveis (ajuste conforme necessário):
     ```
     DB_HOST=localhost
     DB_USER=root
     DB_PASSWORD=
     DB_NAME=enjoei_db
     FLASK_APP=app.py
     FLASK_ENV=development
     ```

5. Inicialize o banco de dados:
   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. Execute o servidor Flask:
   ```
   flask run
   ```

   O servidor estará rodando em `http://127.0.0.1:5000/`

### Frontend (PHP):

[O resto do README permanece o mesmo]

