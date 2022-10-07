import json
from typing import List, Dict


def load_data(path: str) -> List[Dict]:
    """
    Загружает данные из json файла.
    :param path: путь до файла.
    :return: данные в виде списка словарей.
    """
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data
