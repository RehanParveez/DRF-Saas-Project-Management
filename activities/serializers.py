from rest_framework import serializers
from activities.models import Comment, File
from accounts.serializers import UserSerializer1

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['task', 'author', 'content', 'created_at', 'updated_at']
        
class CommentSerializer1(serializers.ModelSerializer):
    author = UserSerializer1(read_only=True)
    class Meta:
        model = Comment
        fields = ["id", "author", "content"]
        
class FileSerializer1(serializers.ModelSerializer):
    uploaded_by = UserSerializer1(read_only=True)
    class Meta:
        model = File
        fields = ["id", "file", "uploaded_by"]
        
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['task', 'file', 'uploaded_by', 'uploaded_at']

