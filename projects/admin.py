from django.contrib import admin
from projects.models import Project, Board

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'organization', 'team', 'description', 'status', 'start_date', 'end_date', 'created_by', 'created_at']
    
@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['name', 'project', 'position', 'created_at']