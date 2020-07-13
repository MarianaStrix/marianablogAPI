import json
import pytest
from django.db import DataError
from rest_framework.exceptions import ErrorDetail

from posts.models import Post


pytestmark = pytest.mark.django_db

ERRORS = {
    "post_with_empty_tags": {
        'tags': [ErrorDetail(string='This field is required.', code='required')]
    },
    "post_with_empty_title": {
        'title': [ErrorDetail(string='This field is required.', code='required')]
    },
    "post_with_empty_text": {
        'text': [ErrorDetail(string='This field is required.', code='required')]
    },
    "post_with_long_title": {
        'title': [ErrorDetail(
            string='Ensure this field has no more than 200 characters.',
            code='max_length')
        ]
    },
}

ERRORS_PATCH = {
    "post_with_empty_tags": {
        'tags': [ErrorDetail(string='This field may not be blank.', code='blank')]
    },
    "post_with_empty_title": {
        'title': [ErrorDetail(string='This field may not be blank.', code='blank')]
    },
    "post_with_empty_text": {
        'text': [ErrorDetail(string='This field may not be blank.', code='blank')]
    },
    "post_with_long_title": {
        'title': [ErrorDetail(
            string='Ensure this field has no more than 200 characters.',
            code='max_length')
        ]
    },
}


class TestModelPost:

    def test_create_post(self, user, posts_data):
        data = {
            "title": posts_data["post_valid"]["title"],
            "text": posts_data["post_valid"]["text"],
            "tags": posts_data["post_valid"]["tags"],
            "author": user["user"],
        }
        post = Post.objects.create(**data)
        for item in data:
            assert data[item] == getattr(post, item)

    def test_create_post_with_long_title(self, user, posts_data):
        data = {
            "title": posts_data["post_valid"]["title"] * 200,
            "text": posts_data["post_valid"]["text"],
            "tags": posts_data["post_valid"]["tags"],
            "author": user["user"],
        }
        try:
            Post.objects.create(**data)
        except DataError as e:
            assert e.args == ('value too long for type character varying(200)\n',)

    def test_create_post_with_empty_tags(self, user, posts_data):
        data = {
            "title": posts_data["post_valid"]["title"],
            "text": posts_data["post_valid"]["text"],
            "author": user["user"],
        }
        post = Post.objects.create(**data)
        for item in data:
            assert data[item] == getattr(post, item)
        assert post.tags.count() == 0


class TestPostViewSet:

    @pytest.mark.parametrize(
        ("post", "status_code", "fields", "errors",),
        [
            ("post_valid", 201, ["title", "text", "tags"], None,),
            ("post_valid", 400, ["text", "tags"], ERRORS["post_with_empty_title"],),
            ("post_valid", 400, ["title", "tags"], ERRORS["post_with_empty_text"],),
            ("post_valid", 400, ["title", "text"], ERRORS["post_with_empty_tags"],),
            ("post_with_long_title", 400, ["title", "text", "tags"], ERRORS["post_with_long_title"],),
        ]
    )
    def test_create_post(
            self, client, user, posts_data, post, status_code, fields, errors
    ):
        client.login(username=user["username"], password=user["password"])
        data = {
            field: json.dumps(posts_data[post][field])
            if field == "tags"
            else posts_data[post][field] for field in fields
        }
        post_url = "/posts/"
        response = client.post(post_url, data)

        if status_code == 201:
            assert response.status_code == status_code
            for item in data:
                if item == "tags":
                    assert response.data[item] == json.loads(data[item])
                else:
                    assert response.data[item] == data[item]
            assert response.data["author"] == user["username"]
        else:
            assert response.status_code == status_code
            assert response.data == errors

    def test_get_post_exist(self, client, user, create_posts):
        client.login(username=user["username"], password=user["password"])
        post_url = "/posts/{0}/".format(create_posts["first_post"].pk)
        response = client.get(post_url)

        assert response.status_code == 200
        for item in create_posts["first_data"]:
            if item == "author":
                assert response.data[item] == create_posts["first_data"][item].username
            else:
                assert response.data[item] == create_posts["first_data"][item]

    def test_get_post_not_exist(self, client, user, create_posts):
        client.login(username=user["username"], password=user["password"])
        max_pk = max([post.pk for post in Post.objects.all()])
        post_url = "/posts/{0}/".format(max_pk + 1)
        response = client.get(post_url)

        assert response.status_code == 404

    def test_get_list_post(self, client, user, create_posts):
        client.login(username=user["username"], password=user["password"])
        post_url = "/posts/"
        response = client.get(post_url)

        assert response.status_code == 200
        list_id = [post['id'] for post in response.data['results']]
        order = sorted(list_id, reverse=True)
        assert list_id == order

    def test_delete_post_exist(self, client, user, create_posts):
        client.login(username=user["username"], password=user["password"])
        post_url = "/posts/{0}/".format(create_posts["first_post"].pk)
        response = client.delete(post_url)

        assert response.status_code == 204
        response = client.get(post_url)
        assert response.status_code == 404

    def test_delete_post_not_exist(self, client, user, create_posts):
        client.login(username=user["username"], password=user["password"])
        max_pk = max([post.pk for post in Post.objects.all()])
        post_url = "/posts/{0}/".format(max_pk + 1)
        response = client.delete(post_url)

        assert response.status_code == 404

    @pytest.mark.parametrize(
        ("post", "status_code", "field", "errors",),
        [
            ("second_post_valid", 200, None, None,),
            ("post_valid", 400, "title", ERRORS_PATCH["post_with_empty_title"],),
            ("post_valid", 400, "text", ERRORS_PATCH["post_with_empty_text"],),
            ("post_valid", 400, "tags", ERRORS_PATCH["post_with_empty_tags"],),
            ("post_with_long_title", 400, None, ERRORS_PATCH["post_with_long_title"],),
        ]
    )
    def test_patch_post(
            self, client, user, posts_data, create_posts,
            post, status_code, field, errors
    ):
        client.login(username=user["username"], password=user["password"])
        data = {
            field: json.dumps(posts_data[post][field]) if field == "tags"
            else posts_data[post][field] for field in ["title", "text", "tags"]
        }
        if field:
            if field == "tags":
                data.update({field:  json.dumps([""])})
            else:
                data.update({field: ""})

        post_url = "/posts/{0}/".format(create_posts["first_post"].pk)
        response = client.patch(post_url, data)

        if status_code == 200:
            assert response.status_code == status_code
            for item in data:
                if item == "tags":
                    assert response.data[item] == json.loads(data[item])
                else:
                    assert response.data[item] == data[item]
            assert response.data["author"] == user["username"]
        else:
            assert response.status_code == status_code
            assert response.data == errors
