from api.models import Post
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'text',
            'date',
            'upvotes',
            'downvotes',
            'post_key',
            'post_type'
        )


class RoastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'text',
            'date',
            'upvotes',
            'downvotes',
            'post_key',
            'post_type'
        )


class BoastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'text',
            'date',
            'upvotes',
            'downvotes',
            'post_key',
            'post_type'
        )
