from rest_framework.generics import ListAPIView
from post.models.post import Post


class PostList(ListAPIView):
    queryset = Post.objects.all()
