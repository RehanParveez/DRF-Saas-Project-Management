from rest_framework import serializers
from tasks.models import Tag, Task, SubTask

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'color', 'organization']
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'project', 'board', 'assignee', 'created_by', 'status', 'due_date', 'tags', 'created_at', 'updated_at']
        
class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['task', 'title', 'is_completed', 'created_at']

