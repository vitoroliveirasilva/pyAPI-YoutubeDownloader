# ========== IMPORTAÇÕES ==========
from flask import Flask # Flask

# ========== APP ==========
def criacao_app():

    # Inicialização do app
    app = Flask(__name__)

    # Blueprint - rotas
    from APIYTDOWNLOAD.routes import register_blueprint
    register_blueprint(app)

    return app


# Criação do objeto app
app = criacao_app()
