# Enjoei Project

Este projeto é um sistema de cadastro e pagamento para a plataforma Enjoei.

## Requisitos

- PHP 7.4 ou superior
- MySQL 5.7 ou superior
- Servidor web (Apache ou Nginx)

## Instalação e Configuração

1. Clone o repositório:
   ```
   git clone https://github.com/iraci2024/enjoei-project.git
   cd enjoei-project
   ```

2. Configure o banco de dados:
   - Acesse o MySQL:
     ```
     mysql -u root -p
     ```
   - Crie o banco de dados 'enjoei_db':
     ```
     CREATE DATABASE enjoei_db;
     ```
   - Crie um usuário e conceda privilégios (substitua 'seu_usuario' e 'sua_senha'):
     ```
     CREATE USER 'seu_usuario'@'localhost' IDENTIFIED BY 'sua_senha';
     GRANT ALL PRIVILEGES ON enjoei_db.* TO 'seu_usuario'@'localhost';
     FLUSH PRIVILEGES;
     ```
   - Saia do MySQL:
     ```
     EXIT;
     ```

3. Configure a conexão com o banco de dados:
   - Edite o arquivo `db_config.php`:
     ```php
     <?php
      = "localhost";
      = "seu_usuario";
      = "sua_senha";
      = "enjoei_db";
     ?>
     ```

4. Importe a estrutura do banco de dados:
   ```
   mysql -u seu_usuario -p enjoei_db < estrutura.sql
   ```
   (Certifique-se de criar o arquivo estrutura.sql com as queries CREATE TABLE mencionadas anteriormente)

5. Configure o servidor web:
   - Para Apache, crie ou edite o arquivo .htaccess na raiz do projeto:
     ```
     RewriteEngine On
     RewriteCond %{REQUEST_FILENAME} !-f
     RewriteCond %{REQUEST_FILENAME} !-d
     RewriteRule ^(.*)$ index.php [QSA,L]
     ```
   - Certifique-se de que o mod_rewrite está habilitado no Apache

## Executando o Backend PHP

1. Se você estiver usando o servidor embutido do PHP para desenvolvimento:
   ```
   php -S localhost:8000
   ```
   Acesse o projeto em http://localhost:8000

2. Se estiver usando Apache ou Nginx, configure o document root para apontar para o diretório do projeto e acesse através do seu localhost.

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

## Processamento de Pagamentos

O sistema atual não processa pagamentos reais. O upload do comprovante é simulado e os dados são apenas armazenados no banco de dados.

## Segurança

- Certifique-se de implementar medidas de segurança adicionais antes de usar em produção
- Use HTTPS para todas as comunicações
- Implemente validação e sanitização de entrada em todos os formulários
- Considere usar prepared statements para todas as queries SQL

## Suporte

Para suporte, entre em contato através do email: contato@suporte-enjoei.online

## Desenvolvimento

Para contribuir com o projeto:

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Faça commit das suas mudanças (`git commit -am 'Adiciona alguma feature'`)
4. Faça push para a branch (`git push origin feature/MinhaFeature`)
5. Crie um novo Pull Request

