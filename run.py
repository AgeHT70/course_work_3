from flask import Flask


# Импортируем блюпринты
from app.posts_bp.views import posts_blueprint


# Создаем экземпляр Flask
app = Flask(__name__)

# Регистрируем блюпринты
app.register_blueprint(posts_blueprint)


@app.errorhandler(404)
def not_found_page(e):
    return "Page not found"


@app.errorhandler(500)
def server_error_page(e):
    return "Server error"


# Запускаем сервер, только если файл запущен, а не импортирован
if __name__ == "__main__":
    app.run()
