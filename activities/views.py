from django.shortcuts import render
from rest_framework import viewsets
from activities.serializers import CommentSerializer, FileSerializer
from activities.models import Comment, File
from organizations.permissions import MemberAdmPermission

# Create your views here.
class CommentViewset(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [MemberAdmPermission]
    
class FileViewset(viewsets.ModelViewSet):
    serializer_class = FileSerializer
    queryset = File.objects.all() 
    permission_classes = [MemberAdmPermission]  

