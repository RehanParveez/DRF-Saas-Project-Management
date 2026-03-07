from django.shortcuts import render
from rest_framework import viewsets
from tasks.serializers import TagSerializer, TaskSerializer, SubTaskSerializer
from tasks.models import Tag, Task, SubTask
from organizations.permissions import MemberAdmPermission, TaskPermission

# Create your views here.
class TagViewset(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    permission_classes = [MemberAdmPermission]
    
class TaskViewset(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()   
    permission_classes = [TaskPermission]
    
class SubTaskViewset(viewsets.ModelViewSet):
    serializer_class = SubTaskSerializer
    queryset = SubTask.objects.all()  
    permission_classes = [TaskPermission]

