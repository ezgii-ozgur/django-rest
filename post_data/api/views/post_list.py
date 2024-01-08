from rest_framework.generics import ListAPIView
from post_data.api.models.post import Post
from post_data.api.serializers.post_serializers import PostSerializer


class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
