# ========== IMPORTAÇÕES ==========
from flask import Flask
import os


# ========== CONFIGURAÇÕES ==========
# Diretório para armazenar vídeos, definindo o caminho absoluto
DOWNLOAD_FOLDER = os.path.abspath("downloads")
# Cria o diretório se não existir
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

# Expressão regular para validar URLs do YouTube
YOUTUBE_URL_PATTERN = r"^(https?\:\/\/)?(www\.)?(youtube\.com|youtu\.?be)\/.+$"

# Tamanho máximo permitido (em MB)
MAX_SIZE_MB = 500


# ========== APP ==========
def criacao_app():
    """Cria a aplicação Flask."""
    app = Flask(__name__)

    # Configurações da aplicação
    app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
    app.config['YOUTUBE_URL_PATTERN'] = YOUTUBE_URL_PATTERN
    app.config['MAX_SIZE_MB'] = MAX_SIZE_MB

    # Blueprint - rotas
    from APIYTDOWNLOAD.routes import register_blueprint
    register_blueprint(app)

    return app


# Criação do objeto app
app = criacao_app()
