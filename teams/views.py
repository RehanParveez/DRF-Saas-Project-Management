from django.shortcuts import render
from rest_framework import viewsets
from teams.serializers import TeamSerializer
from teams.models import Team
from organizations.permissions import TeamAdmPermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.
class TeamViewset(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    permission_classes = [TeamAdmPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['name', 'description']
    ordering_fields = ['created_at']
    filterset_fields = ['name', 'description', 'created_at']
    
    def get_queryset(self):
        return Team.objects.filter(organization__memberships__user=self.request.user, organization__memberships__is_active=True).distinct()
    
   

