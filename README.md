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
