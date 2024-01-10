from rest_framework.generics import CreateAPIView
from comment.api.models.comment import Comment
from comment.api.serializers.comment_create_serializer import CommentCreateSerializer


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
