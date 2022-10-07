import json


class PostsDAO:

    def __init__(self, path):
        self.path = path

    def load_data(self):
        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_all(self):
        posts = self.load_data()
        return posts

    def get_by_pk(self, pk):
        for post in self.load_data():
            if pk == int(post["pk"]):
                return post

    def get_by_username(self, username):
        posts = [post for post in self.load_data()
                 if username.lower() == post["poster_name"].lower()]
        if not posts:
            raise ValueError("Нет такого пользователя")
        return posts

    def get_by_keyword(self, keyword):
        posts = [post for post in self.load_data()
                 if keyword.lower() in post["content"].lower()]
        return posts

    def create_tag(self, post_pk):
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
