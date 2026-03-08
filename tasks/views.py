from django.shortcuts import render
from rest_framework import viewsets
from tasks.serializers import TagSerializer, TaskSerializer, SubTaskSerializer
from tasks.models import Tag, Task, SubTask
from organizations.permissions import MemberAdmPermission, TaskPermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from tasks.pagination import TaskPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from activities.models import Comment


# Create your views here.
class TagViewset(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    permission_classes = [MemberAdmPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['name']
    filterset_fields = ['name', 'color']
    pagination_class = TaskPagination
    
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
    pagination_class = TaskPagination
    
    def get_queryset(self):
      return Task.objects.filter(project__organization__memberships__user=self.request.user, project__organization__memberships__is_active=True).distinct()
  
    @action(detail=True, methods=['post'])
    def task(self, request, pk=None):
      task = self.get_object()
      user_id = request.data.get('user_id')
      
      user = User.objects.filter(id=user_id).first()
      if not user:
        return Response({'err': 'no user'}, status=404)
        task.assignee = user
        task.save()
      return Response({'msg': 'task not given'})
  
    @action(detail=True, methods=['post'])
    def status(self, request, pk=None):
      task = self.get_object()
      status_value = request.data.get('status')
      task.status = status_value
      task.save()
      return Response({'msg': 'task is updated'})
    
    @action(detail=True, methods=['post'])
    def completed(self, request, pk=None):
      task = self.get_object()
      task.status = 'completed'
      task.save() 
      return Response({'msg': 'task is completed'})

    @action(detail=True, methods=['post'])
    def comment(self, request, pk=None):
      task = self.get_object()
      content = request.data.get('content')
      Comment.objects.create(task=task, user=request.user, content=content)
      return Response({'msg': 'have some shame friend'})
    
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
    pagination_class = TaskPagination
    
    def get_queryset(self):
        return SubTask.objects.filter(task__project__organization__memberships__user=self.request.user, task__project__organization__memberships__is_active=True).distinct()

