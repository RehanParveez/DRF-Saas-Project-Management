from django.contrib import admin
from activities.models import Comment, File

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['task', 'author', 'content', 'created_at', 'updated_at']
    
@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['task', 'file', 'uploaded_by', 'uploaded_at']
