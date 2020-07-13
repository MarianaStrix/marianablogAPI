import pytest

from accounts.models import Account
from posts.models import Post


pytestmark = pytest.mark.django_db


class TestModelAccount:

    def test_create_account_with_avatar(self, user_data):
        username = user_data["user_with_avatar"]["username"]
        password = user_data["user_with_avatar"]["password"]
        avatar = user_data["user_with_avatar"]["avatar"]
        user = Account.objects.create_user(
            username=username,
            password=password,
            avatar=avatar,
        )

        assert user.username == username
        assert user.avatar == avatar

    def test_create_account_without_avatar(self, user_data):
        username = user_data["user_with_avatar"]["username"]
        password = user_data["user_with_avatar"]["password"]
        user = Account.objects.create_user(
            username=username,
            password=password,
        )

        assert user.username == username
        assert user.avatar.name == "default.png"


class TestAccountViewSet:

    def test_get_account(self, client, user):
        client.login(username=user["username"], password=user["password"])
        account_url = "/accounts/{0}/".format(user["user"].pk)
        response = client.get(account_url)

        assert response.status_code == 200
        assert response.data == {
            "url": "http://testserver/accounts/{0}/".format(user["user"].pk),
            "id": user["user"].pk,
            "username": user["username"],
            "posts": [],
            "avatar": "http://testserver/media/default.png",
        }

    def test_get_account_from_another_user(self, client, user, second_user):
        client.login(username=second_user["username"], password=second_user["password"])
        account_url = "/accounts/{0}/".format(user["user"].pk)
        response = client.get(account_url)

        assert response.status_code == 200
        assert response.data == {
            "url": "http://testserver/accounts/{0}/".format(user["user"].pk),
            "id": user["user"].pk,
            "username": user["username"],
            "posts": [],
            "avatar": "http://testserver/media/default.png",
        }

    def test_get_account_not_login(self, client, user):
        account_url = "/accounts/{0}/".format(user["user"].pk)
        response = client.get(account_url)

        assert response.status_code == 200
        assert response.data == {
            "url": "http://testserver/accounts/{0}/".format(user["user"].pk),
            "id": user["user"].pk,
            "username": user["username"],
            "posts": [],
            "avatar": "http://testserver/media/default.png",
        }

    def test_patch_account(self, client, user):
        client.login(username=user["username"], password=user["password"])
        account_url = "/accounts/{0}/".format(user["user"].pk)
        new_username = "new_username"

        response = client.patch(account_url, {"username": new_username})
        assert response.status_code == 200

        response = client.get(account_url)
        assert response.data["username"] == new_username

        response = client.get("/auth/user/")
        assert response.data["username"] == new_username

    def test_patch_another_account(self, client, user, second_user):
        client.login(username=second_user["username"], password=second_user["password"])
        account_url = "/accounts/{0}/".format(user["user"].pk)
        new_username = "new_username"

        response = client.patch(account_url, {"username": new_username})
        assert response.status_code == 403

        response = client.get(account_url)
        assert response.data["username"] == user["username"]

    def test_get_account_posts(self, client, user):
        client.login(username=user["username"], password=user["password"])
        Post.objects.create(
            title="Title",
            text="Text",
            author=user["user"],
        )
        account_url = "/accounts/{0}/".format(user["user"].pk)
        response = client.get(account_url)

        assert response.status_code == 200
        assert response.data == {
            "url": "http://testserver/accounts/{0}/".format(user["user"].pk),
            "id": user["user"].pk,
            "username": user["username"],
            "posts": ['http://testserver/posts/1/'],
            "avatar": "http://testserver/media/default.png",
        }
