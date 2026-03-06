from django.shortcuts import render
from rest_framework import viewsets
from notifications.serializers import ActivitySerializer , NotificationSerializer
from notifications.models import Activity, Notification

# Create your views here.
class ActivityViewset(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()  
    
class NotificationViewset(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
    
 

