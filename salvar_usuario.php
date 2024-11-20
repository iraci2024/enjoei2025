<?php
include 'db_config.php';
include 'functions.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nome = $_POST['nome'];
    $email = $_POST['email'];
    $telefone = $_POST['telefone'];

    if (salvar_usuario($nome, $email, $telefone)) {
        echo json_encode(["success" => true, "message" => "Usuário cadastrado com sucesso"]);
    } else {
        echo json_encode(["success" => false, "message" => "Erro ao cadastrar usuário"]);
    }
} else {
    echo json_encode(["success" => false, "message" => "Método não permitido"]);
}
?>