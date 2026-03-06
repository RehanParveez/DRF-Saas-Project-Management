from rest_framework import serializers
from teams.models import Team
from accounts.serializers import UserSerializer1

class TeamSerializer(serializers.ModelSerializer):
    user = UserSerializer1(read_only=True)
    class Meta:
        model = Team
        fields = ['name', 'organization', 'user', 'description', 'members', 'created_by', 'created_at']
        
