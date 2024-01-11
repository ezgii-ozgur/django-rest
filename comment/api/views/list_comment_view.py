from rest_framework.generics import ListAPIView
from comment.api.models.comment import Comment
from comment.api.serializers.comment_list_serializer import CommentListSerializer


class CommentListAPIView(ListAPIView):
    serializer_class = CommentListSerializer

    def get_queryset(self):
        return Comment.objects.filter(parent = None)