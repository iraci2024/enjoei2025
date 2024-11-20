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
