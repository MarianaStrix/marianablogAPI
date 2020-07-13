import json
import os

import pytest
from rest_framework.test import APIClient

from accounts.models import Account


TESTS_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user():
    path = os.path.join(TESTS_DIR, "data/users.json")
    with open(path) as f:
        data = json.load(f)
        username = data["user_valid"]["username"]
        password = data["user_valid"]["password"]
        user = Account.objects.create_user(
            username=username,
            password=password,
        )
        return {
            "username": username,
            "password": password,
            "user": user,
        }


@pytest.fixture
def second_user():
    path = os.path.join(TESTS_DIR, "data/users.json")
    with open(path) as f:
        data = json.load(f)
        username = data["second_user_valid"]["username"]
        password = data["second_user_valid"]["password"]
        user = Account.objects.create_user(
            username=username,
            password=password,
        )
        return {
            "username": username,
            "password": password,
            "user": user,
        }
