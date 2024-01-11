from rest_framework.serializers import ModelSerializer
from comment.api.models.comment import Comment


class CommentChildSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
