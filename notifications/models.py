from django.db import models
from accounts.models import User
from tasks.models import Task

# Create your models here.
class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activity')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='activity')
    work = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.work
    
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.message
    
class ApiRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.method} {self.path}'
