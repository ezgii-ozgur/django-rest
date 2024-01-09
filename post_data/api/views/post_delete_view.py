from rest_framework.generics import DestroyAPIView
from post_data.api.models.post import Post
from post_data.api.permissions.custom_permissions import IsOwner
from post_data.api.serializers.post_serializer import PostSerializer


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwner]


