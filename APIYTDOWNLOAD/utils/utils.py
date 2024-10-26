from flask import jsonify
import os
import re


# Substitui caracteres não permitidos
def renomeacao(filename):
    return re.sub(r'[<>:"/\\|?*\s]+', '_', filename)


# Remove o arquivo do sistema de arquivos
def remove_arquivo(file_path):
    os.remove(file_path)


# Trata erros durante o download do vídeo
def erro_download(e):
    error_message = "Ocorreu um erro inesperado."

    # Erro específico
    if "regex_search" in str(e):
        error_message = "Não foi possível acessar o vídeo. Verifique a URL ou tente novamente mais tarde."
    
    return jsonify({"erro": error_message}), 500
