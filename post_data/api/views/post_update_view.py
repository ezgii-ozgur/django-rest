from rest_framework.generics import RetrieveUpdateAPIView
from post_data.api.models.post import Post
from post_data.api.serializers.post_serializer import PostSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from post_data.api.permissions.custom_permissions import IsOwner


class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwner]

    def perform_update(self, serializer):
        serializer.save(mofied_by_user=self.request.user)
