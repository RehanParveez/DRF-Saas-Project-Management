from django.contrib import admin
from organizations.models import Organization, Membership

# Register your models here.
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'slug', 'owner', 'created_at', 'updated_at']
    
@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ['user', 'organization', 'control', 'joined_at', 'is_active']
    
