from rest_framework.generics import DestroyAPIView
from comment.api.models.comment import Comment
from comment.api.serializers.comment_update_delete_serializer import CommentUpdateDeleteSerializer
from comment.api.permissions.custom_permission import IsOwner


class CommentDeleteAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentUpdateDeleteSerializer
    lookup_field = 'pk'
    permission_classes = [IsOwner]
