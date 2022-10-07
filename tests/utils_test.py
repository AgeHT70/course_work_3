from typing import List, Dict

import pytest

from config import POSTS_PATH
from utils import load_data


def test_load_data():
    data = load_data(POSTS_PATH)
    assert type(data) == list, 'возвращает не список'
    assert type(data[0]) == dict, 'возвращает не словарь'
