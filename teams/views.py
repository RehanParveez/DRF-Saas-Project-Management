from django.shortcuts import render
from rest_framework import viewsets
from teams.serializers import TeamSerializer
from teams.models import Team

# Create your views here.
class TeamViewset(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    
 

