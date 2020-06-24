from api.models import Post
from rest_framework import serializers
# from rest_framework.serializers import HyperlinkedModelSerializer


class PostSerializer(serializers.HyperlinkedModelSerializer):
    # post_type = serializers.BooleanField()
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
