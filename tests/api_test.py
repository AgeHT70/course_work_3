valid_keys = {"poster_name",
              "poster_avatar",
              "pic",
              "content",
              "views_count",
              "likes_count",
              "pk"
              }


class TestApi:

    def test_api_posts(self, test_client):
        """
        Проверяем получаем правильный тип данных и необходимый набор ключей
        """
        response = test_client.get("/api/posts")
        assert type(response.json) == list, "Возвращает не список"
        for i in range(len(response.json)):
            assert set(response.json[i].keys()) == set(valid_keys), "Неверный список ключей"

    def test_api_posts_by_pk(self, test_client):
        """
        Проверяем получаем правильный тип данных и необходимый набор ключей
        """
        response = test_client.get(f"/api/posts/1")
        assert type(response.json) == dict, "Возвращает не словарь"
        assert set(response.json.keys()) == set(valid_keys), "Неверный список ключей"

