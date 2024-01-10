from rest_framework import serializers
from post_data.api.models.post import Post


class PostSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='post:detail',
        lookup_field='slug'
    )
    user_name = serializers.SerializerMethodField()

    def get_user_name(self, obj):
        return str(obj.user.username)

    class Meta:
        model = Post
        fields = [
            'user_name',
            'title',
            'content',
            'image',
            'url',
            'created_date',
            'modified_by_user'
        ]

