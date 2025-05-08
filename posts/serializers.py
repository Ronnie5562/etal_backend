from rest_framework import serializers
from .models import (
    Post,
    Tag,
    PostLike,
    PostComment
)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'created_at']


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ['id', 'user', 'post', 'created_at']


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = ['id', 'user', 'post', 'text', 'created_at', 'updated_at']


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    media = serializers.URLField(source='media.url', read_only=True)

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'text', 'media', 'tags', 'likes_count',
            'comments', 'comments_count', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_comments_count(self, obj):
        return obj.comments.count()
