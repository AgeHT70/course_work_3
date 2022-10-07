from utils import load_data


class PostsDAO:

    def __init__(self, posts_path: str, comments_path: str):
        self.posts_path = posts_path
        self.comments_path = comments_path

    def get_all(self) -> list[dict]:
        """
        Получаем все посты из файла.
        :return:
        """
        posts = load_data(self.posts_path)
        return posts

    def get_by_pk(self, pk: int) -> dict:
        """
        Получаем один пост по еко номеру.
        :param pk: номер поста.
        :return: один пост.
        """
        for post in load_data(self.posts_path):
            if pk == int(post["pk"]):
                return post

    def get_by_username(self, username: str) -> list[dict]:
        """
        Получаем все посты для одного пользователя.
        :param username: имя пользователя.
        :return: список постов.
        """
        posts = [post for post in load_data(self.posts_path)
                 if username.lower() == post["poster_name"].lower()]
        if not posts:
            raise ValueError("Нет такого пользователя")
        return posts

    def get_by_keyword(self, keyword: str) -> list[dict]:
        """
        Ищем все посты по ключевому слову.
        :param keyword: слово для поиска.
        :return: список постов.
        """
        posts = [post for post in load_data(self.posts_path)
                 if keyword.lower() in post["content"].lower()]
        return posts

    def create_tag(self, post_pk: int) -> dict:
        """
        Из слова начинающегося с "#" делаем ссылку.
        :param post_pk: номер поста.
        :return: измененный пост.
        """
        post = self.get_by_pk(post_pk)
        content_list = post["content"].split()
        for i in range(len(content_list)):
            if content_list[i].startswith('#'):
                word = content_list[i]
                content_list[i] = word.replace(word,
                                               f'<a href="/tag/{word[1:]}"'
                                               f'>{word}</a>')
        post["content"] = ' '.join(content_list)
        return post

    def get_comments_by_post_pk(self, post_pk: int) -> list[dict]:
        """
        Получаем все комментарии по номеру поста из файла.
        :param post_pk: номер поста.
        :return: список комментариев.
        """
        comments = [comment for comment in load_data(self.comments_path)
                    if post_pk == int(comment["post_id"])]
        if not self.get_by_pk(post_pk):
            raise ValueError("Нет такого поста")
        elif not comments:
            return []
        return comments
