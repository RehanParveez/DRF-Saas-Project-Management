from rest_framework import serializers
from organizations.models import Organization, Membership
from accounts.serializers import UserSerializer1

class MembershipSerializer1(serializers.ModelSerializer):
    user = UserSerializer1(read_only=True)
    class Meta:
        model = Membership
        fields = ['user', 'control', 'joined_at']
        
class OrganizationSerializer(serializers.ModelSerializer):
    memberships = MembershipSerializer1(many=True, read_only=True)
    class Meta:
        model = Organization
        fields = ['name', 'description', 'slug', 'owner', 'memberships', 'created_at', 'updated_at']
        
class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ['user', 'organization', 'control', 'joined_at', 'is_active']
        
        