from django.contrib import admin
from notifications.models import Activity, Notification

# Register your models here.
@admin.register(Activity)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['user', 'task', 'work', 'created_at']
    
@admin.register(Notification)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['user', 'message', 'is_read', 'created_at']