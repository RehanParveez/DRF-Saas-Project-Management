from django.shortcuts import render
from rest_framework import viewsets
from notifications.serializers import ActivitySerializer , NotificationSerializer
from notifications.models import Activity, Notification
from organizations.permissions import TeamAdmPermission, MemberAdmPermission

# Create your views here.
class ActivityViewset(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()  
    permission_classes = [TeamAdmPermission]
    
class NotificationViewset(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
    permission_classes = [MemberAdmPermission]
    
 

