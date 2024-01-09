from rest_framework import serializers
from post_data.api.models.post import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'user',
            'title',
            'content',
            'image',
            'slug',
            'created_date',
            'modified_by_user'
        ]
