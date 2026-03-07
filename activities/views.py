from django.shortcuts import render
from rest_framework import viewsets
from activities.serializers import CommentSerializer, FileSerializer
from activities.models import Comment, File
from organizations.permissions import MemberAdmPermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.
class CommentViewset(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [MemberAdmPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['content']
    ordering_fields = ['created_at']
    filterset_fields = ['content', 'created_at']
    
    def get_queryset(self):
       return Comment.objects.filter(task__project__organization__memberships__user=self.request.user, task__project__organization__memberships__is_active=True).distinct()
    
class FileViewset(viewsets.ModelViewSet):
    serializer_class = FileSerializer
    queryset = File.objects.all() 
    permission_classes = [MemberAdmPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    ordering_fields = ['uploaded_at']
    filterset_fields = ['uploaded_at']  
    
    def get_queryset(self):
       return File.objects.filter(task__project__organization__memberships__user=self.request.user, task__project__organization__memberships__is_active=True).distinct()

