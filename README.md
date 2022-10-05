# Курсовая работа SkyPro 3 курс

1) Необходимые функции оформлены в posts_dao и comments_dao и тесты к ним
2) В posts_blueprint реализованы представления
```
"/" - главная страница
"/post/<int:pk>" - пост по pk
"/users/<username>" - посты по username
"/search" - поиск по слову
```
3) В api_blueprint реализованы представления
```
/api/posts
/api/posts/<int:post_id>
```
4) Реализован обработчик ошибок 404 и 500
5) Залогированы обращения к эндпоинтам API
6) Добавлены тесты на API 