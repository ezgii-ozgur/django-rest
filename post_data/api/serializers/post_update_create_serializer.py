from rest_framework import serializers
from post_data.api.models.post import Post


class PostUpdateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
        ]
