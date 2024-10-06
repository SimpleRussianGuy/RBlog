import os
from flask import Blueprint, request, render_template, redirect, url_for, flash, current_app
from werkzeug.utils import secure_filename

main = Blueprint('main', __name__)

# Разрешённые расширения файлов
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

# Главная страница, обработка загрузки файлов
@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Проверка наличия файла в запросе
        if 'file' not in request.files:
            flash('Файл не найден')
            return redirect(request.url)

        file = request.files['file']

        # Если пользователь не выбрал файл
        if file.filename == '':
            flash('Файл не выбран')
            return redirect(request.url)

        # Если файл разрешён и успешно загружен
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            flash('Файл успешно загружен')
            return redirect(url_for('main.index'))

    # Вывод списка загруженных файлов
    try:
        files = os.listdir(current_app.config['UPLOAD_FOLDER'])
        # Фильтруем только разрешённые файлы
        files = [f for f in files if allowed_file(f)]
    except FileNotFoundError:
        files = []

    return render_template('index.html', files=files)