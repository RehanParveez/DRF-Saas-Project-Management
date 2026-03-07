from django.shortcuts import render
from rest_framework import viewsets
from organizations.serializers import OrganizationSerializer, MembershipSerializer
from organizations.models import Organization, Membership
from organizations.permissions import OrgAdmPermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.
class OrganizationViewset(viewsets.ModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    permission_classes = [OrgAdmPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    search_fields = ['name', 'slug']
    ordering_fields = ['created_at']
    filterset_fields = ['name', 'description', 'slug', 'created_at']
    
    def get_queryset(self):
        return Organization.objects.filter(memberships__user=self.request.user, memberships__is_active=True).distinct()
    
class MembershipViewset(viewsets.ModelViewSet):
    serializer_class = MembershipSerializer
    queryset = Membership.objects.all()   
    permission_classes = [OrgAdmPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filtering fields
    ordering_fields = ['joined_at']
    filterset_fields = ['joined_at', 'is_active']
    
    def get_queryset(self):
        return Membership.objects.filter(organization__memberships__user=self.request.user, organization__memberships__is_active=True).distinct()
