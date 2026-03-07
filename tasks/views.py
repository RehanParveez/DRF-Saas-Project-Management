from django.shortcuts import render
from rest_framework import viewsets
from tasks.serializers import TagSerializer, TaskSerializer, SubTaskSerializer
from tasks.models import Tag, Task, SubTask
from organizations.permissions import MemberAdmPermission, TaskPermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.
class TagViewset(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    permission_classes = [MemberAdmPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['name']
    filterset_fields = ['name', 'color']
    
    def get_queryset(self):
        return Tag.objects.filter(organization__memberships__user=self.request.user, organization__memberships__is_active=True).distinct()
    
class TaskViewset(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()   
    permission_classes = [TaskPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']
    filterset_fields = ['title', 'description', 'status', 'due_date', 'created_at']
    
    def get_queryset(self):
      return Task.objects.filter(project__organization__memberships__user=self.request.user, project__organization__memberships__is_active=True).distinct()
    
class SubTaskViewset(viewsets.ModelViewSet):
    serializer_class = SubTaskSerializer
    queryset = SubTask.objects.all()  
    permission_classes = [TaskPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['title']
    ordering_fields = ['created_at']
    filterset_fields = ['title', 'is_completed', 'created_at']
    
    def get_queryset(self):
        return SubTask.objects.filter(task__project__organization__memberships__user=self.request.user, task__project__organization__memberships__is_active=True).distinct()

