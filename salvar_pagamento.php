<?php
include 'db_config.php';
include 'functions.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $valor = 199.00; // Valor fixo conforme a página
    $comprovante = $_FILES['comprovante'];

    $comprovante_path = upload_comprovante($comprovante);

    if ($comprovante_path) {
        // Aqui você deve obter o ID do usuário de alguma forma, por exemplo, de uma sessão
        $usuario_id = 1; // Exemplo: usuário com ID 1

        if (salvar_pagamento($usuario_id, $valor, $comprovante_path)) {
            echo json_encode(["success" => true, "message" => "Pagamento registrado com sucesso"]);
        } else {
            echo json_encode(["success" => false, "message" => "Erro ao registrar pagamento"]);
        }
    } else {
        echo json_encode(["success" => false, "message" => "Erro ao fazer upload do comprovante"]);
    }
} else {
    echo json_encode(["success" => false, "message" => "Método não permitido"]);
}
?>