from rest_framework.generics import CreateAPIView
from post_data.api.models.post import Post
from post_data.api.serializers.post_serializer import PostSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
