from rest_framework.generics import UpdateAPIView
from comment.api.models.comment import Comment
from comment.api.serializers.comment_update_delete_serializer import CommentUpdateDeleteSerializer
from comment.api.permissions.custom_permission import IsOwner


class CommentUpdateAPIView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentUpdateDeleteSerializer
    lookup_field = 'pk'
    permission_classes = [IsOwner]

    def perform_update(self, serializer):
        serializer.save(mofied_by_user=self.request.user)
