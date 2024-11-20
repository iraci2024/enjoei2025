
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
from dotenv import load_dotenv
from datetime import datetime
import pymysql

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL').replace('mysql://', 'mysql+pymysql://')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'txt'}
db = SQLAlchemy(app)

# Configurar PyMySQL para ser usado com SQLAlchemy
pymysql.install_as_MySQLdb()

def allowed_file(filename):
    return '.' in filename and            filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(255), nullable=False)

    def set_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def check_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)

class Pagamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    data = db.Column(db.DateTime, nullable=False)
    valor = db.Column(db.Float, nullable=False)
    comprovante_path = db.Column(db.String(255), nullable=True)

@app.route('/registro', methods=['POST'])
def registro():
    data = request.json
    if Usuario.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'Email já cadastrado'}), 400
    
    novo_usuario = Usuario(email=data['email'])
    novo_usuario.set_senha(data['senha'])
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify({'message': 'Usuário registrado com sucesso'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    usuario = Usuario.query.filter_by(email=data['email']).first()
    if usuario and usuario.check_senha(data['senha']):
        return jsonify({'message': 'Login bem-sucedido', 'user_id': usuario.id}), 200
    return jsonify({'message': 'Credenciais inválidas'}), 401

@app.route('/upload_comprovante', methods=['POST'])
def upload_comprovante():
    if 'file' not in request.files:
        return jsonify({'message': 'Nenhum arquivo enviado'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'Nenhum arquivo selecionado'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        usuario_id = request.form.get('usuario_id')
        valor = request.form.get('valor')
        
        novo_pagamento = Pagamento(
            usuario_id=usuario_id,
            data=datetime.now(),
            valor=float(valor),
            comprovante_path=filepath
        )
        db.session.add(novo_pagamento)
        db.session.commit()
        
        return jsonify({'message': 'Comprovante enviado com sucesso'}), 201
    return jsonify({'message': 'Tipo de arquivo não permitido'}), 400

if __name__ == '__main__':
    print("Iniciando a aplicação...")
    print(f"URL do banco de dados: {app.config['SQLALCHEMY_DATABASE_URI']}")
    print("Tentando criar as tabelas...")
    with app.app_context():
        db.create_all()
    print("Tabelas criadas com sucesso!")
    print("Configuração concluída.")
    print("O servidor Flask está pronto para ser iniciado.")
