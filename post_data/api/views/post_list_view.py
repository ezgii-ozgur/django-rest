from rest_framework.generics import ListAPIView
from post_data.api.models.post import Post
from rest_framework.filters import SearchFilter, OrderingFilter
from post_data.api.serializers.post_serializer import PostSerializer
from post_data.api.paginations.post_pagination import PostPagination


class PostListAPIView(ListAPIView):
    # qudueryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title','content']
    pagination_class = PostPagination

    def get_queryset(self):
        query_set = Post.objects.filter(draft=False)
        return query_set

