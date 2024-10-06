import os
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Загружаем конфигурацию из config.py или instance/config.py
    app.config.from_pyfile('config.py', silent=True)

    # Проверяем наличие папки для загрузки файлов
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Регистрируем Blueprint
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app