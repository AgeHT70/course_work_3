import json

from utils import load_data


class BookmarksDAO:

    def __init__(self, path):
        self.path = path

    def write_to_json(self, bookmarks: list[dict]) -> None:
        """
        Записывает данные в файл.
        :param bookmarks:
        :return:
        """
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(bookmarks, file, ensure_ascii=False)

    def get_all(self):
        """
        Загружает все bookmarks из файла.
        :return: список bookmarks.
        """
        bookmarks = load_data(self.path)
        return bookmarks

    def add(self, post: dict) -> None:
        """
        Записывает bookmark в файл.
        :param post: словарь
        :return: None
        """
        bookmarks = self.get_all()

        if post not in bookmarks:
            bookmarks.append(post)
            self.write_to_json(bookmarks)

    def del_bookmark(self, post_pk: int) -> None:
        """
        Удалаяет bookmark по номеру поста из файла.
        :param post_pk: номер поста.
        :return: None
        """
        bookmarks = self.get_all()
        bookmarks = [bookmark for bookmark in bookmarks
                     if int(bookmark["pk"]) != post_pk]

        self.write_to_json(bookmarks)


