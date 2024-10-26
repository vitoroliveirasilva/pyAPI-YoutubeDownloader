# Importação do blueprint
from .yt_routes import ytdownload_bp

# Registro do blueprint
def register_blueprint(app):
    app.register_blueprint(ytdownload_bp)
