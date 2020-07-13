import json
import os

import pytest

from posts.models import Post


TESTS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@pytest.fixture
def posts_data():
    path = os.path.join(TESTS_DIR, "data/posts.json")
    with open(path) as f:
        posts_data = json.load(f)
        return posts_data


@pytest.fixture
def create_posts(user, second_user, posts_data):
    first_data = {
        "title": posts_data["post_valid"]["title"],
        "text": posts_data["post_valid"]["text"],
        "author": user["user"],
    }
    first_post = Post.objects.create(**first_data)

    second_data = {
        "title": posts_data["post_valid"]["title"],
        "text": posts_data["post_valid"]["text"],
        "author": second_user["user"],
    }
    second_post = Post.objects.create(**second_data)

    return {
        "first_post": first_post,
        "first_data": first_data,
        "second_post": second_post,
        "second_data": second_data,
    }
