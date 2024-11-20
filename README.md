# Enjoei Project

Este projeto é um sistema de cadastro e pagamento para a plataforma Enjoei.

## Requisitos

- PHP 7.4 ou superior
- MySQL 5.7 ou superior
- Servidor web (Apache ou Nginx)

## Instalação

1. Clone o repositório:
   ```
   git clone https://github.com/iraci2024/enjoei-project.git
   cd enjoei-project
   ```

2. Configure o banco de dados:
   - Crie um banco de dados MySQL
   - Edite o arquivo `db_config.php` com as credenciais do seu banco de dados

3. Importe a estrutura do banco de dados:
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

4. Configure o servidor web:
   - Aponte o document root para o diretório do projeto
   - Certifique-se de que o PHP está configurado corretamente

## Uso

1. Acesse a página inicial (home.html) através do seu navegador
2. Preencha o formulário de cadastro
3. Na página de pagamento, faça o upload do comprovante
4. Você será redirecionado para a página de agradecimento

## Estrutura do Projeto

- `home.html`: Página inicial com formulário de cadastro
- `pagamento.html`: Página de pagamento com upload de comprovante
- `obrigado.html`: Página de agradecimento
- `db_config.php`: Configurações de conexão com o banco de dados
- `functions.php`: Funções auxiliares para processamento de dados
- `salvar_usuario.php`: Script para salvar dados do usuário
- `salvar_pagamento.php`: Script para processar o pagamento e upload do comprovante

## Suporte

Para suporte, entre em contato através do email: contato@suporte-enjoei.online
