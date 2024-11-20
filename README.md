# Enjoei Project

Este projeto é um sistema de cadastro e pagamento para a plataforma Enjoei.

## Requisitos

- PHP 7.4 ou superior
- MySQL 5.7 ou superior
- Servidor web (Apache ou XAMPP para Windows)

## Instalação e Configuração (Windows)

1. Clone ou faça o download do repositório para seu computador local.

2. Se você estiver usando XAMPP:
   - Mova a pasta do projeto para o diretório 'htdocs' do XAMPP.
   - Inicie o Apache e o MySQL no painel de controle do XAMPP.

3. Configure o banco de dados:
   - Abra o phpMyAdmin (geralmente em http://localhost/phpmyadmin)
   - Crie um novo banco de dados chamado 'enjoei_db'
   - Selecione o banco de dados 'enjoei_db' e vá para a aba 'SQL'
   - Execute as seguintes queries para criar as tabelas necessárias:

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

4. Configure a conexão com o banco de dados:
   - Abra o arquivo `db_config.php` no diretório do projeto
   - Edite as informações de conexão:
     ```php
     <?php
      = "localhost";
      = "root";  // ou o usuário que você configurou
      = "";      // a senha do seu MySQL, se houver
      = "enjoei_db";
     ?>
     ```

## Executando o Projeto

1. Se você está usando XAMPP:
   - O projeto deve estar acessível em `http://localhost/nome-da-pasta-do-projeto`

2. Se você está usando o servidor embutido do PHP:
   - Abra o prompt de comando na pasta do projeto
   - Execute: `php -S localhost:8000 (ou outra porta disponível, como 8001)`
   - Acesse o projeto em `http://localhost:8000 (ou a porta que você escolheu)`

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

- Este é um projeto de demonstração. Para uso em produção, implemente medidas de segurança adicionais.
- Use HTTPS para todas as comunicações em um ambiente de produção.
- Implemente validação e sanitização de entrada em todos os formulários.
- Use prepared statements para todas as queries SQL para prevenir injeção de SQL.

## Resolução de Problemas

- Se encontrar erros de conexão com o banco de dados, verifique se as credenciais em `db_config.php` estão corretas.
- Certifique-se de que o PHP tem permissões para escrever no diretório de uploads.
- Para erros relacionados ao MySQL, verifique se o serviço está rodando.

## Suporte

Para suporte, entre em contato através do email: contato@suporte-enjoei.online
