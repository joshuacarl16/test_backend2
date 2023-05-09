from rest_framework import fields, serializers
from django.contrib.auth import get_user_model
from .models import Category, Topic, Comment

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = "__all__"
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class TopicSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()

    class Meta:
        model = Topic
        fields = ['id', 'user', 'category', 'title', 'content', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    topic = TopicSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'user', 'topic', 'content', 'created_at']