from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('post_id', 'category', 'title', 'author', 'content', 'excerpt', 'slug', 'status')


