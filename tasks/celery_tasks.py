from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from tasks.models import Task
from datetime import timedelta

@ shared_task
def task_email(email, task_title):
    subject = 'giving new task'
    message = f'new task is given {task_title}'
    send_mail(subject, message, settings.EMAIL_HOST_USER, [email], fail_silently=True)
    return 'email is sent'

@shared_task
def daily_task():
    today = timezone.localdate()
    due_task = Task.objects.filter(due_date=today, assignee__isnull=False)
    
    for task in due_task:
        task_email.delay(task.assignee.email, task.title)
    return f'{due_task.count()}'

@shared_task
def weekly_report():
    today = timezone.localdate()
    week_ago = today - timedelta(days=7)
    tasks = Task.objects.filter(created_at__date__gte = week_ago, created_at__date__lte = today, assignee__isnull=False)

    for task in tasks:
        subject = 'weekly report'
        message = task.assignee.username + 'task'+ task.title + 'has status' + task.status
        send_mail(subject, message, settings.EMAIL_HOST_USER, [task.assignee.email], fail_silently=True)
    return 'weekly report is sent'

    