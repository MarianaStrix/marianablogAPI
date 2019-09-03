from django.contrib.auth import get_user_model
from rest_framework import serializers


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='post-detail',
        read_only=True,
    )

    class Meta:
        model = get_user_model()
        fields = ('url', 'id', 'username', 'posts', 'avatar',)
