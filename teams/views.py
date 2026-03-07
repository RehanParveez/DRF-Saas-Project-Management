from django.shortcuts import render
from rest_framework import viewsets
from teams.serializers import TeamSerializer
from teams.models import Team
from organizations.permissions import TeamAdmPermission

# Create your views here.
class TeamViewset(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    permission_classes = [TeamAdmPermission]
    
 

