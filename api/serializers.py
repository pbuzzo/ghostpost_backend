from api.models import Post
from rest_framework.serializers import HyperlinkedModelSerializer


class PostSerializer(HyperlinkedModelSerializer):
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
