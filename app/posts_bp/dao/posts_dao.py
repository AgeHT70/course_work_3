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
