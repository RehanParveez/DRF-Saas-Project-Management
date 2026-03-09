from django.db.models.signals import post_save
from django.dispatch import receiver
from tasks.models import Task
from notifications.models import Activity, Notification
from activities.models import Comment

@receiver(post_save, sender=Task)
def creating_task(sender, instance, created, **kwargs):
    if created:
        action = 'task is created'
    else:
        action = 'task is updated'
    Activity.objects.create(task=instance, user=instance.created_by, work=f'{action} {instance.title}')
    
@receiver(post_save, sender=Comment)
def comment_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance.task.created_by, message=f'{instance.author.username} commented {instance.task.title}')