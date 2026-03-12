from accounts.tests import ParentTest
from django.contrib.auth import get_user_model
from organizations.models import Organization
from projects.models import Project
from projects.models import Board
from tasks.models import Task

# Create your tests here.
class ReportViewsetTest(ParentTest):
    def setUp(self):
        super().setUp()
    
        User = get_user_model()
        self.user2 = User.objects.create_user(username = 'user2', email = 'user2@gmail.com', password = 'pass12312')
        self.organization = Organization.objects.create(name = 'test organization', slug = 'test-organization', owner = self.user)
        self.project = Project.objects.create(name = 'test project', organization=self.organization)
        self.board = Board.objects.create(name= 'main board', project=self.project, position=1)
        Task.objects.create(title = 'task1', project=self.project, board=self.board, assignee=self.user, created_by=self.user, status='done')
        Task.objects.create(title = 'task2', project=self.project, board=self.board, assignee=self.user, created_by=self.user, status='working')
        Task.objects.create(title = 'task3', project=self.project, board=self.board, assignee=self.user2, created_by=self.user, status='done')
        
    def test_completed_task(self):
      response = self.client.get('/reports/report/completed_task/')
      self.assertEqual(response.status_code, 200)
      data = response.json()
      self.assertEqual(len(data), 2)
        
    def test_progress(self):
      response = self.client.get(f'/reports/report/{self.project.id}/progress/')
      self.assertEqual(response.status_code, 200)
      data = response.json()
      self.assertEqual(data['tot_tasks'], 3)
      self.assertEqual(data['comple_tasks'], 2)
      
    def test_work(self):
      response = self.client.get('/reports/report/work/')
      self.assertEqual(response.status_code, 200)
      data = response.json()
      self.assertEqual(len(data), 2)
      
    def test_project_tasks(self):
      response = self.client.get('/reports/report/project_tasks/')
      self.assertEqual(response.status_code, 200)
      data = response.json()
      self.assertEqual(data[0]['project'], 'test project')
      self.assertEqual(data[0]['total_tasks'], 3)
    
    
    