from api.serializers import PostSerializer
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
        ##### END #####

    @action(detail=False)
    def highest_rated(self, request):
        highest_rated = Post.objects.all().order_by('downvotes', '-upvotes')
        serializer = self.get_serializer(highest_rated, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def boast(self, request):
        boast = Post.objects.filter(post_type=True)
        serializer = self.get_serializer(boast, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def roast(self, request):
        roast = Post.objects.filter(post_type=False)
        serializer = self.get_serializer(roast, many=True)
        return Response(serializer.data)
