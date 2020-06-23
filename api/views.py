from api.serializers import PostSerializer
from api.models import Post
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    basename = 'post'
    queryset = Post.objects.all()


class PostView(ModelViewSet):
    serializer_class = PostSerializer
    basename = 'postview'
    queryset = Post.objects.all()
    
    # https://www.django-rest-framework.org/api-guide/viewsets/#marking-extra-actions-for-routing
    @action(detail=True, methods=['get'])
    def upvote(self, request, pk=None):
        vote = Post.objects.get(pk=pk)
        vote.net_votes += 1
        vote.save()
        return Response({'status': 'Post was upvoted!'})

    @action(detail=True, methods=['get'])
    def downvote(self, request, pk=None):
        vote = Post.objects.get(pk=pk)
        vote.net_votes -= 1
        vote.save()
        return Response({'status': 'Post was downvoted!'})
