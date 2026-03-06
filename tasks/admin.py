from django.contrib import admin
from tasks.models import Tag, Task, SubTask
# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'color', 'organization']
    
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'project', 'board', 'assignee', 'created_by', 'status', 'due_date', 'created_at', 'updated_at']
    
@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ['task', 'title', 'is_completed', 'created_at']