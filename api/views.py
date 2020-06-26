from api.serializers import PostSerializer, RoastSerializer, BoastSerializer
from api.models import Post
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    basename = 'post'
    queryset = Post.objects.all()

    # https://www.django-rest-framework.org/api-guide/viewsets/#marking-extra-actions-for-routing
    @action(detail=True, methods=['get'])
    def upvote(self, request, pk=None):
        vote = Post.objects.get(pk=pk)
        vote.upvotes += 1
        vote.save()
        return Response({'status': 'Post was upvoted!'})

    @action(detail=True, methods=['get'])
    def downvote(self, request, pk=None):
        vote = Post.objects.get(pk=pk)
        vote.downvotes += 1
        vote.save()
        return Response({'status': 'Post was downvoted!'})


class BoastViewSet(ModelViewSet):
    serializer_class = BoastSerializer
    basename = 'boasts'
    queryset = Post.objects.filter(post_type=True)


class RoastViewSet(ModelViewSet):
    serializer_class = RoastSerializer
    basename = 'roasts'
    queryset = Post.objects.filter(post_type=False)
