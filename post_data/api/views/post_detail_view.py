from rest_framework.generics import RetrieveAPIView
from post_data.api.models.post import Post
from post_data.api.serializers.post_serializer import PostSerializer


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
