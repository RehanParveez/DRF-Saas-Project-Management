from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from tasks.models import Task
from django.db.models import Count, Q
from rest_framework.response import Response
from django.db import connection

# Create your views here.
class ReportViewset(viewsets.ViewSet):
    
    @action(detail=False, methods=['get'])
    def completed_task(self, request):
        result = (Task.objects.filter(status='done').values('assignee__username').annotate(compl_tasks=Count('id')))
        return Response(result)
    
    @action(detail=True, methods=['get'])
    def progress(self, request, pk=None):
        tot_tasks = Task.objects.filter(project_id=pk).count()
        comple_tasks = Task.objects.filter(project_id=pk, status='done').count()
        
        if tot_tasks > 0:
           progress = (comple_tasks / tot_tasks) * 100
        else:
            progress = 0
        return Response({'tot_tasks': tot_tasks, 'comple_tasks': comple_tasks, 'progress': progress})
    
    @action(detail=False, methods=['get'])
    def work(self, request):
        result = (Task.objects.values('assignee__username').annotate(comple_tasks = Count('id', filter=Q(status='done')),
            tot_tasks = Count('id')))
        return Response(result)
    
    @action(detail=False, methods=['get'])
    def project_tasks(self, request):
        
        with connection.cursor() as cursor:
            cursor.execute('''
                 SELECT proj.name, COUNT(task.id)   
                 FROM tasks_task task
                 JOIN projects_project proj ON task.project_id = proj.id
                 GROUP BY proj.name      
            ''')
            rows = cursor.fetchall()
            
        return Response([{'project': row[0], 'total_tasks': row[1]} for row in rows])
        
    
    
    
    
        
        
