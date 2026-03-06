from rest_framework import serializers
from activities.models import Comment, File

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['task', 'author', 'content', 'created_at', 'updated_at']
        
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['task', 'file', 'uploaded_by', 'uploaded_at']

