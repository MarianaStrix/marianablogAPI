from rest_framework import serializers
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer

from .models import Post


class PostSerializer(TaggitSerializer, serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    tags = TagListSerializerField()

    class Meta:
        model = Post
        fields = ('url', 'id', 'author', 'title', 'text', 'tags', 'published_date')
