from flask import Flask

# Импортируем блюпринты
from app.posts.views import posts_blueprint
from app.api.views import api_blueprint
from app.bookmarks.views import bookmarks_blueprint


# Создаем экземпляр Flask
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# Регистрируем блюпринты
app.register_blueprint(posts_blueprint)
app.register_blueprint(api_blueprint)
app.register_blueprint(bookmarks_blueprint)


#Обработчики ошибок 404 и 500
@app.errorhandler(404)
def not_found_page(e):
    return "Page not found"


@app.errorhandler(500)
def server_error_page(e):
    return "Server error"


# Запускаем сервер, только если файл запущен, а не импортирован
if __name__ == "__main__":
    app.run()

