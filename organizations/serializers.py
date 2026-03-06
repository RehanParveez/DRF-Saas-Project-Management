from rest_framework import serializers
from organizations.models import Organization, Membership

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['name', 'description', 'slug', 'owner', 'created_at', 'updated_at']
        
class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ['user', 'organization', 'control', 'joined_at', 'is_active']

