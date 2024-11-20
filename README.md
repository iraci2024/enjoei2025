<<<<<<< HEAD
# Enjoei Project

Este projeto é um sistema de cadastro e pagamento para a plataforma Enjoei, otimizado para ambiente Windows.

## Requisitos

- Windows 10 ou superior
- XAMPP (com PHP 7.4 ou superior e MySQL 5.7 ou superior)

## Instalação e Configuração (Windows)

1. Instalação do XAMPP:
   - Baixe e instale o XAMPP do site oficial: https://www.apachefriends.org/index.html
   - Durante a instalação, certifique-se de selecionar Apache, MySQL e PHP.

2. Configuração do Projeto:
   - Faça o download do projeto e extraia-o para C:\xampp\htdocs\enjoei

3. Configuração do Banco de Dados:
   - Inicie o XAMPP Control Panel e start os serviços Apache e MySQL
   - Abra o navegador e acesse http://localhost/phpmyadmin
   - Crie um novo banco de dados chamado 'enjoei_db'
   - Selecione o banco de dados 'enjoei_db' e vá para a aba 'SQL'
   - Cole e execute as seguintes queries:

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

4. Configuração da Conexão com o Banco de Dados:
   - Navegue até C:\xampp\htdocs\enjoei
   - Abra o arquivo `db_config.php` com um editor de texto (como o Notepad++)
   - Edite as informações de conexão:
     ```php
     <?php
      = "localhost";
      = "root";
      = "";
      = "enjoei_db";
     ?>
     ```

5. Configuração de Permissões:
   - Crie uma pasta chamada 'uploads' em C:\xampp\htdocs\enjoei
   - Clique com o botão direito na pasta 'uploads', vá em Propriedades > Segurança
   - Clique em 'Editar' e depois em 'Adicionar'
   - Digite 'Everyone', clique em 'Verificar Nomes' e depois em 'OK'
   - Marque 'Controle Total' para o grupo 'Everyone' e clique em 'Aplicar' e 'OK'

## Executando o Projeto

1. Usando XAMPP:
   - Certifique-se de que os serviços Apache e MySQL estão rodando no XAMPP Control Panel
   - Abra o navegador e acesse http://localhost/enjoei

2. Usando o servidor embutido do PHP:
   - Abra o Prompt de Comando como administrador
   - Navegue até o diretório do projeto: `cd C:\xampp\htdocs\enjoei`
   - Execute: `php -S localhost:8000` (ou outra porta disponível, como 8001)
   - Acesse o projeto em `http://localhost:8000` (ou a porta que você escolheu)

## Estrutura do Projeto

- `index.php`: Ponto de entrada da aplicação
- `home.html`: Página inicial com formulário de cadastro
- `pagamento.html`: Página de pagamento com upload de comprovante
- `obrigado.html`: Página de agradecimento
- `db_config.php`: Configurações de conexão com o banco de dados
- `functions.php`: Funções auxiliares para processamento de dados
- `salvar_usuario.php`: Script para salvar dados do usuário
- `salvar_pagamento.php`: Script para processar o pagamento e upload do comprovante

## Uso

1. Acesse a página inicial (home.html) através do seu navegador
2. Preencha o formulário de cadastro
3. Na página de pagamento, faça o upload do comprovante
4. Você será redirecionado para a página de agradecimento

## Resolução de Problemas

- Se encontrar erros de conexão com o banco de dados, verifique se o MySQL está rodando no XAMPP Control Panel
- Para erros de "permissão negada" ao fazer upload, verifique as permissões da pasta 'uploads'
- Se as páginas não carregarem, certifique-se de que o Apache está rodando no XAMPP Control Panel

## Suporte

Para suporte, entre em contato através do email: contato@suporte-enjoei.online
=======
# Enjoei2025 - Backend

Este é o backend para o projeto Enjoei, uma plataforma de vendas online.

## Requisitos

- Python 3.8+
- MySQL 8.0+
- pip (gerenciador de pacotes do Python)

## Instalação

1. Clone o repositório:
   ```
   git clone https://github.com/iraci2024/enjoei2025.git
   cd enjoei2025
   ```

2. Crie um ambiente virtual e ative-o:
   ```
   python3 -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

4. Configure o banco de dados MySQL:
   - Crie um banco de dados chamado `enjoei_db`
   - Atualize o arquivo `.env` com suas credenciais do MySQL:
     ```
     DATABASE_URL=mysql://username:password@localhost/enjoei_db
     ```

5. Inicialize o banco de dados:
   ```
   python3 app.py
   ```

## Uso

Para iniciar o servidor:

```
python3 -m flask run --host=0.0.0.0 --port=5001
```

O servidor estará rodando em `http://localhost:5001`.

## Endpoints da API

- `POST /registro`: Registra um novo usuário
- `POST /login`: Autentica um usuário
- `POST /upload_comprovante`: Faz upload de um comprovante de pagamento

## Exemplo de uso

### Registro de usuário

```bash
curl -X POST -H "Content-Type: application/json" -d '{"email":"usuario@example.com","senha":"senha123"}' http://localhost:5001/registro
```

### Login

```bash
curl -X POST -H "Content-Type: application/json" -d '{"email":"usuario@example.com","senha":"senha123"}' http://localhost:5001/login
```

### Upload de comprovante

```bash
curl -X POST -F "file=@caminho/do/arquivo.pdf" -F "usuario_id=1" -F "valor=100.00" http://localhost:5001/upload_comprovante
```

## Estrutura do Projeto

- `app.py`: Arquivo principal da aplicação Flask
- `requirements.txt`: Lista de dependências do projeto
- `.env`: Arquivo de configuração com variáveis de ambiente
- `uploads/`: Diretório onde os comprovantes de pagamento são armazenados

## Contribuindo

Por favor, leia o arquivo CONTRIBUTING.md para detalhes sobre nosso código de conduta e o processo para enviar pull requests.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE.md para detalhes.
>>>>>>> bd8c4b700d161e93063aea5cea5f2bc28c37e957
