from django.shortcuts import render
from rest_framework import viewsets
from accounts.serializers import UserSerializer
from accounts.models import User
from organizations.permissions import OrgAdmPermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.
class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [OrgAdmPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['email', 'profession']
    ordering_fields = ['created_at']
    filterset_fields = ['email', 'profession', 'phone']
    
    def get_queryset(self):
        return User.objects.filter(memberships__organization__memberships__user=self.request.user).distinct()
    
    
