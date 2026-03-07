from django.shortcuts import render
from rest_framework import viewsets
from notifications.serializers import ActivitySerializer , NotificationSerializer
from notifications.models import Activity, Notification
from organizations.permissions import TeamAdmPermission, MemberAdmPermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.
class ActivityViewset(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()  
    permission_classes = [TeamAdmPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['work']
    ordering_fields = ['created_at']
    filterset_fields = ['work', 'created_at']
    
    def get_queryset(self):
      return Activity.objects.filter(task__project__organization__memberships__user=self.request.user, task__project__organization__memberships__is_active=True).distinct()
    
class NotificationViewset(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
    permission_classes = [MemberAdmPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['message']
    ordering_fields = ['created_at']
    filterset_fields = ['message', 'is_read', 'created_at']
    
    def get_queryset(self):
       return Notification.objects.filter(user=self.request.user)
    
 

