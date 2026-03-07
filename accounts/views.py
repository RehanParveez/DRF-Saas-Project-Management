from django.shortcuts import render
from rest_framework import viewsets
from accounts.serializers import UserSerializer
from accounts.models import User
from organizations.permissions import OrgAdmPermission

# Create your views here.
class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [OrgAdmPermission]
    
    
