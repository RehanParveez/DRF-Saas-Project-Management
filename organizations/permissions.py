from rest_framework.permissions import BasePermission
from organizations.models import Membership
from rest_framework.permissions import SAFE_METHODS

class SupAdmPermission(BasePermission):
    def has_permission(self, request, view):
        return Membership.objects.filter(user=request.user, control='supadm', is_active=True).exists()
    
    def has_object_permission(self, request, view, obj):
        return Membership.objects.filter(user=request.user, control='supadm', is_active=True).exists()
    
class OrgAdmPermission(BasePermission):
    def has_permission(self, request, view):
        return Membership.objects.filter(user=request.user, control__in=['supadm', 'orgadm'], is_active=True).exists()
    
    def has_object_permission(self, request, view, obj):
        return Membership.objects.filter(user=request.user, organization=obj.organization, control__in=['supadm', 'orgadm'], is_active=True).exists()
    
class TeamAdmPermission(BasePermission):
    def has_permission(self, request, view):
        return Membership.objects.filter(user=request.user, control__in=['supadm', 'orgadm', 'teamadm'], is_active=True).exists()
    
    def has_object_permission(self, request, view, obj):
        return Membership.objects.filter(user=request.user, organization=obj.organization, control__in=['supadm', 'orgadm', 'teamadm'], is_active=True).exists()
    
class MemberAdmPermission(BasePermission):
    def has_permission(self, request, view):
        return Membership.objects.filter(user=request.user, control__in=['supadm', 'orgadm', 'teamadm', 'memberadm'], is_active=True).exists()
    
    def has_object_permission(self, request, view, obj):
        return Membership.objects.filter(user=request.user, organization=obj.organization, control__in=['supadm', 'orgadm', 'teamadm', 'memberadm'], is_active=True).exists()
    
class ViewerAdmPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method not in SAFE_METHODS:
            return False
        return Membership.objects.filter(user=request.user, is_active=True).exists()
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return False
    
class TaskPermission(BasePermission):
    def has_permission(self, request, view):
        return Membership.objects.filter(user=request.user, is_active=True).exists()
    
    def has_object_permission(self, request, view, obj):
        membership = Membership.objects.filter(user=request.user, organization=obj.project.organization, is_active=True).first()
        if not membership:
            return False
        role = membership.control
        if request.method in SAFE_METHODS:
            return True
        if role in ['supadm', 'orgadm']:
            return True
        if role == 'teamadm':
            return True
        if role == 'memberadm' and obj.assignee == request.user:
            return True
        return False