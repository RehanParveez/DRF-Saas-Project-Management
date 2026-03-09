from django.contrib import admin
from notifications.models import Activity, Notification, ApiRequest

# Register your models here.
@admin.register(Activity)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['user', 'task', 'work', 'created_at']
    
@admin.register(Notification)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['user', 'message', 'is_read', 'created_at']
    
@admin.register(ApiRequest)
class ApiRequestAdmin(admin.ModelAdmin):
    list_display = ['user', 'method', 'path', 'created_at']