from accounts.tests import ParentTest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from organizations.models import Organization
from projects.models import Project, Board
from tasks.models import Task

class TaskTestBase(ParentTest):
    def setUp(self):
        super().setUp()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        
        User = get_user_model()
        self.assignee = User.objects.create_user(username = 'assignee', email = 'assigneegmail.com', password = 'pass12312')
        self.organization = Organization.objects.create(name ='organization test', owner=self.user, slug='org-test')
        self.project = Project.objects.create(name='project test', organization=self.organization, created_by = self.user)
        self.board = Board.objects.create(name='board1', project = self.project, position = 1)
        
class TaskViewsetTest(TaskTestBase):
    def test_create(self):
        data = {
            'title': 'task test',
            'description': 'create test',
            'project': self.project.id,
            'board': self.board.id,
            'assignee': self.assignee.id,
            'status': 'pending'
            }
        response = self.client.post('/tasks/tasks/', data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().title, 'task test')

    def test_list(self):
        Task.objects.create(title='Task1', description='list test', project=self.project, board=self.board, assignee=self.assignee, created_by=self.user, status='pending')
        response = self.client.get('/tasks/tasks/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), Task.objects.filter(project=self.project).count())

