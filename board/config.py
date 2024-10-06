import os

# Основные настройки
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static/uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Секретный ключ для флэшей и сессий
SECRET_KEY = 'dev'