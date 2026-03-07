from rest_framework import serializers
from tasks.models import Tag, Task, SubTask
from activities.serializers import CommentSerializer1, FileSerializer1

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'color', 'organization']
 
class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['task', 'title', 'is_completed', 'created_at']     
           
class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubTaskSerializer(many=True, read_only=True)
    comments = CommentSerializer1(many=True, read_only=True)
    files = FileSerializer1(many=True, read_only=True)
    class Meta:
        model = Task
        fields = ['title', 'description', 'project', 'board', 'assignee', 'comments', 'subtasks', 'files', 'created_by', 'status', 'due_date', 'tags', 'created_at', 'updated_at']
              
