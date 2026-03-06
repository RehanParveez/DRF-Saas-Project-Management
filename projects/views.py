from django.shortcuts import render
from rest_framework import viewsets
from projects.serializers import ProjectSerializer, BoardSerializer
from projects.models import Project, Board

# Create your views here.
class ProjectViewset(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    
class BoardViewset(viewsets.ModelViewSet):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()   
