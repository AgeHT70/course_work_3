import json


class CommentsDao:

    def __init__(self, path):
        self.path = path

    def load_data(self):
        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_by_post_pk(self, post_pk):
        comments = [comment for comment in self.load_data() if post_pk == int(comment["post_id"])]
        return comments

