from flask import Flask


# Импортируем блюпринты
from app.posts_bp.views import posts_blueprint


# Создаем экземпляр Flask
app = Flask(__name__)

# Регистрируем блюпринты
app.register_blueprint(posts_blueprint)

# Запускаем сервер, только если файл запущен, а не импортирован
if __name__ == "__main__":
    app.run()
