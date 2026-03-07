from django.shortcuts import render
from rest_framework import viewsets
from projects.serializers import ProjectSerializer, BoardSerializer
from projects.models import Project, Board
from organizations.permissions import TeamAdmPermission, MemberAdmPermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.
class ProjectViewset(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [TeamAdmPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['name', 'description']
    ordering_fields = ['created_at']
    filterset_fields = ['name', 'status', 'start_date', 'end_date' 'created_at']
    
    def get_queryset(self):
        return Project.objects.filter(organization__memberships__user=self.request.user, organization__memberships__is_active=True).distinct()
    
class BoardViewset(viewsets.ModelViewSet):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()   
    permission_classes = [MemberAdmPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['name']
    ordering_fields = ['created_at']
    filterset_fields = ['name', 'position', 'created_at']
    
    def get_queryset(self):
        return Board.objects.filter(project__organization__memberships__user=self.request.user, project__organization__memberships__is_active=True).distinct()
