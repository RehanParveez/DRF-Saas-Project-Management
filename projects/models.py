from django.db import models
from organizations.models import Organization
from teams.models import Team
from accounts.models import User

class Project(models.Model):
    STATUS_CHOICES = (
        ('designing', 'Designing'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('pending', 'Pending'),
    )
    name = models.CharField(max_length=25)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='projects')
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='projects')
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_projects')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Board(models.Model):
    name = models.CharField(max_length=25)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='boards')
    position = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name