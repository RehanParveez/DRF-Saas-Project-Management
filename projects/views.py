from django.shortcuts import render
from rest_framework import viewsets
from projects.serializers import ProjectSerializer, BoardSerializer
from projects.models import Project, Board
from organizations.permissions import TeamAdmPermission, MemberAdmPermission

# Create your views here.
class ProjectViewset(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [TeamAdmPermission]
    
class BoardViewset(viewsets.ModelViewSet):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()   
    permission_classes = [MemberAdmPermission]
