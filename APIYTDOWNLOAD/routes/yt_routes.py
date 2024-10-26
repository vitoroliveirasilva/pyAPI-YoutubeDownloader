# ========== IMPORTAÇÕES ==========
from flask import Blueprint, request, jsonify, send_file, current_app
from pytubefix import YouTube
import re
import os
import threading
from ..utils import renomeacao, remove_arquivo, erro_download


# Configuração do blueprint para a rota
ytdownload_bp = Blueprint("ytdownload", __name__)


# Rota para download do vídeo
@ytdownload_bp.route('/download_video', methods=['POST'])
def download_video():
    """Rota para download de vídeos do YouTube."""
    
    # Obtém o JSON recebido e extrai a URL
    data = request.get_json()
    video_url = data.get("url")

    # Verifica se a URL foi fornecida
    if not video_url:
        return jsonify({"erro": "URL não fornecida"}), 400

    # Valida o formato da URL do YouTube
    if not re.match(current_app.config['YOUTUBE_URL_PATTERN'], video_url):
        return jsonify({"erro": "URL inválida"}), 400

    try:
        # Baixa o vídeo usando a biblioteca pytubefix
        yt_video = YouTube(video_url)
        video_stream = yt_video.streams.get_highest_resolution()

        # Verifica se o stream é válido
        if video_stream is None:
            return jsonify({"erro": "Não foi possível encontrar a melhor resolução."}), 500

        # Valida o tamanho do vídeo
        if video_stream.filesize > current_app.config['MAX_SIZE_MB'] * 1024 * 1024:  # Converte MB para bytes
            return jsonify({"erro": f"O tamanho do vídeo excede o limite de {current_app.config['MAX_SIZE_MB']} MB"}), 400

        # Caminho para salvar o vídeo, renomeando o nome do arquivo
        safe_filename = renomeacao(f"{yt_video.title}.mp4")
        file_path = os.path.join(current_app.config['DOWNLOAD_FOLDER'], safe_filename)
        
        # Baixa o vídeo e salva no caminho especificado
        video_stream.download(output_path=current_app.config['DOWNLOAD_FOLDER'], filename=safe_filename)
        
        # Envia o arquivo de vídeo como resposta
        response = send_file(file_path, as_attachment=True)

        # Remove o arquivo após 60 segundos
        threading.Timer(60.0, remove_arquivo, args=[file_path]).start()
        
        return response
    
    except Exception as e:
        # Tratamento de erros
        return erro_download(e)
