from django.db import models
from organizations.models import Organization
from accounts.models import User

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=25)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='teams')
    description = models.TextField()
    members = models.ManyToManyField(User, related_name="teams")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='teams')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
