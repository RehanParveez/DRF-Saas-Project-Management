from django.db import models
from projects.models import Project, Board
from organizations.models import Organization
from accounts.models import User

class Tag(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='tags')

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('working', 'Working'),
        ('done', 'Done'),
    )
    title = models.CharField(max_length=25)
    description = models.TextField(blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='tasks')
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='assigned_tasks')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_tasks')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    due_date = models.DateField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='tasks', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title

class SubTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    title = models.CharField(max_length=25)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title