import json
import os

import pytest


TESTS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@pytest.fixture
def user_data():
    path = os.path.join(TESTS_DIR, "data/users.json")
    with open(path) as f:
        user_data = json.load(f)
        return user_data


