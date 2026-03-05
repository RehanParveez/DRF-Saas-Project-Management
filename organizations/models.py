from django.db import models
from accounts.models import User

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organizations')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Membership(models.Model):
    CONTROL_CHOICES = (
        ('supadm', 'SupAdm'),
        ('orgadm', 'OrgAdm'),
        ('teamadm', 'TeamAdm'),
        ('memberadm', 'MemberAdm'),
        ('vieweradm', 'ViewerAdm'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='memberships')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='memberships')
    control = models.CharField(choices=CONTROL_CHOICES, default='vieweradm')
    joined_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ['user', 'organization']
    
    def __str__(self):
        return self.user
    
    
    