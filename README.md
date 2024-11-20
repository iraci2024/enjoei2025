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

2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

3. Configure as variáveis de ambiente no arquivo `.env`:
   ```
   DB_HOST=seu_host
   DB_USER=seu_usuario
   DB_PASSWORD=sua_senha
   DB_NAME=enjoei_db
   ```

4. Execute o servidor Flask:
   ```
   python app.py
   ```

### Frontend (PHP):

1. Configure o servidor web (Apache ou XAMPP) para apontar para o diretório do projeto.

2. Configure o banco de dados:
   - Crie um banco de dados 'enjoei_db'
   - Execute as seguintes queries SQL:

     ```sql
     CREATE TABLE usuarios (
       id INT AUTO_INCREMENT PRIMARY KEY,
       nome VARCHAR(255) NOT NULL,
       email VARCHAR(255) NOT NULL,
       telefone VARCHAR(20) NOT NULL
     );

     CREATE TABLE pagamentos (
       id INT AUTO_INCREMENT PRIMARY KEY,
       usuario_id INT NOT NULL,
       valor DECIMAL(10, 2) NOT NULL,
       comprovante_path VARCHAR(255) NOT NULL,
       FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
     );
     ```

3. Configure a conexão com o banco de dados no arquivo `db_config.php`.

## Estrutura do Projeto

- `app.py`: Arquivo principal da aplicação Flask (Backend)
- `index.php`: Ponto de entrada da aplicação PHP (Frontend)
- `home.html`: Página inicial com formulário de cadastro
- `pagamento.html`: Página de pagamento com upload de comprovante
- `obrigado.html`: Página de agradecimento
- `db_config.php`: Configurações de conexão com o banco de dados (PHP)
- `functions.php`: Funções auxiliares para processamento de dados (PHP)
- `salvar_usuario.php`: Script para salvar dados do usuário (PHP)
- `salvar_pagamento.php`: Script para processar o pagamento e upload do comprovante (PHP)
- `requirements.txt`: Lista de dependências do projeto Python
- `.env`: Arquivo de configuração com variáveis de ambiente (Python)
- `uploads/`: Diretório onde os comprovantes de pagamento são armazenados

## Uso

1. Inicie o servidor backend Flask.
2. Acesse a página inicial (home.html) através do seu navegador.
3. Preencha o formulário de cadastro.
4. Na página de pagamento, faça o upload do comprovante.
5. Você será redirecionado para a página de agradecimento.

## API Endpoints (Backend)

- `POST /registro`: Registra um novo usuário
- `POST /login`: Autentica um usuário
- `POST /upload_comprovante`: Faz upload de um comprovante de pagamento

## Suporte

Para suporte, entre em contato através do email: contato@suporte-enjoei.online

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE.md para detalhes.
