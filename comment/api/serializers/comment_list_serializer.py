from rest_framework.serializers import ModelSerializer, SerializerMethodField
from comment.api.models.comment import Comment
from comment.api.serializers.comment_child_serializer import CommentChildSerializer


class CommentListSerializer(ModelSerializer):
    replies = SerializerMethodField()
    class Meta:
        model = Comment
        fields = '__all__'

    def get_replies(self, obj):
        if obj.any_children:
            return CommentListSerializer(obj.children(), many=True).data
