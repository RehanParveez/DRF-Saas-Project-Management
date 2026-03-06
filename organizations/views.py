from django.shortcuts import render
from rest_framework import viewsets
from organizations.serializers import OrganizationSerializer, MembershipSerializer
from organizations.models import Organization, Membership

# Create your views here.
class OrganizationViewset(viewsets.ModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    
class MembershipViewset(viewsets.ModelViewSet):
    serializer_class = MembershipSerializer
    queryset = Membership.objects.all()   
