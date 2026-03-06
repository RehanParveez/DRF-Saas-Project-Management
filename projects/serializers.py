from rest_framework import serializers
from projects.models import Project, Board

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'organization', 'team', 'description', 'status', 'start_date', 'end_date', 'created_by', 'created_at']
        
class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['name', 'project', 'position', 'created_at']

