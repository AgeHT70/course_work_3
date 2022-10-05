import json


class BookmarksDAO:

    def __init__(self, path):
        self.path = path

    def load_data(self):
        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_all(self):
        bookmarks = self.load_data()
        return bookmarks

    def add(self, post):
        bookmarks = self.load_data().append(post)
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(bookmarks, file, ensure_ascii=False)
        pass