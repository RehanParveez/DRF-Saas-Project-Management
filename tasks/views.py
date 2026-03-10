from django.shortcuts import render
from rest_framework import viewsets
from tasks.serializers import TagSerializer, TaskSerializer, SubTaskSerializer
from tasks.models import Tag, Task, SubTask
from organizations.permissions import MemberAdmPermission, TaskPermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from tasks.pagination import TaskPagination
from rest_framework.decorators import action
from accounts.models import User
from rest_framework.response import Response
from activities.models import Comment
from django.db import transaction
from notifications.models import Activity
from tasks.celery_tasks import task_email
from django.core.cache import cache

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
    
    def list(self, request, *args, **kwargs):
      print('calling task list view')
      key = f'tasks{request.user.id}'
      cached_data = cache.get(key)
      
      if cached_data:
        print('returned from cache')
        return Response(cached_data)
      
      print('getting from db and caching')
      queryset = self.get_queryset()
      serializer = self.get_serializer(queryset, many=True)
      cache.set(key, serializer.data, 50)
      return Response(serializer.data)
    
    @transaction.atomic
    def create(self, request, *args, **kwargs):
       serializer = self.get_serializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       task = serializer.save()
       subtasks = request.data.get('subtasks')
       
       if subtasks:
           for subtask in subtasks:
               SubTask.objects.create(task=task, title=subtask.get('title'), is_completed=False)
               
       cache.delete(f'tasks{request.user.id}')
       
       Activity.objects.create(user=request.user, task=task, work='task is created')
       if task.assignee:
         task_email.delay(task.assignee.email, task.title)
       return Response(serializer.data)
   
    @transaction.atomic
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
    
    @transaction.atomic
    @action(detail=True, methods=['post'])
    def status(self, request, pk=None):
      task = self.get_object()
      status_value = request.data.get('status')
      task.status = status_value
      task.save()
      return Response({'msg': 'task is updated'})
    
    @transaction.atomic
    @action(detail=True, methods=['post'])
    def completed(self, request, pk=None):
      task = self.get_object()
      task.status = 'done'
      task.save() 
      return Response({'msg': 'task is completed'})
    
    @transaction.atomic
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

