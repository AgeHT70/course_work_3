import pytest

from app.posts.dao.posts_dao import PostsDAO
from config import POSTS_PATH, COMMENTS_PATH


comments_keys = [
    "post_id",
    "commenter_name",
    "comment",
    "pk",
]

posts_keys = [
    "poster_name",
    "poster_avatar",
    "pic",
    "content",
    "views_count",
    "likes_count",
    "pk",
]

posts = PostsDAO(POSTS_PATH, COMMENTS_PATH)


class TestPostsDao:

    def test_get_all(self):
        """
        Проверяем тип результата.
        Проверяем правильность возвращаемых ключей поста.
        """
        data = posts.get_all()
        assert type(data) == list
        assert type(data[0]) == dict
        assert set(data[0].keys()) == set(posts_keys)

    def test_get_by_pk(self):
        """
        Проверяем тип результата.
        Проверяем правильность возвращаемого поста.
        """
        assert type(posts.get_by_pk(1)) == dict
        assert posts.get_by_pk(1)["pk"] == 1

    def test_get_by_username(self):
        """
        Проверяем тип результата.
        Проверяем правильность возвращаемого результата
        """
        assert type(posts.get_by_username("leo")) == list
        assert posts.get_by_username("leo")[0]["poster_name"] == "leo"

    def test_get_by_username_exceptions(self):
        """
        Проверяем исключение ValueError по несуществующему имени пользователя
        поста
        """
        with pytest.raises(ValueError):
            posts.get_by_username("!!!")

    def test_get_by_keyword(self):
        """
        Проверяем является ли результат списком.
        Есть ли искомое слово в контенте найденного поста.
        :return:
        """
        result = posts.get_by_keyword("еда")
        assert type(posts.get_by_keyword(" ")) == list
        assert "еда" in result[0]["content"]

    def test_get_comments_by_post_pk(self):
        """
        Проверяем тип результата.
        Проверяем правильность возвращаемых ключей комментариев
        """
        comments = posts.get_comments_by_post_pk(1)
        assert type(comments) == list
        assert set(comments[0].keys()) == set(comments_keys)

    def test_get_comments_by_post_pk_exception(self):
        """
        Проверяем исключение ValueError по несуществующему номеру поста
        """
        with pytest.raises(ValueError):
            posts.get_comments_by_post_pk(0)
