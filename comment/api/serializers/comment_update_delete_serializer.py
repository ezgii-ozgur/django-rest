from rest_framework.serializers import ModelSerializer
from comment.api.models.comment import Comment


class CommentUpdateDeleteSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'content'
        ]
