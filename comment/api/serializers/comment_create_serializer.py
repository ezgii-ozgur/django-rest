from rest_framework.serializers import ModelSerializer, ValidationError
from comment.api.models.comment import Comment


class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['created_date', ]

    def validate(self, attrs):
        if attrs["parent"]:
            if attrs["parent"].post != attrs[["post"]]:
                raise ValidationError("Something went wrong !!")
        return attrs
