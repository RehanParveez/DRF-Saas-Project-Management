from accounts.tests import ParentTest
from django.contrib.auth import get_user_model
from organizations.models import Organization, Membership
from projects.models import Project, Board
from tasks.models import Task
from notifications.models import Activity

class TaskTestBase(ParentTest):
    def setUp(self):
        super().setUp()
        
        User = get_user_model()
        self.assignee = User.objects.create_user(username = 'assignee', email = 'assignee@gmail.com', password = 'pass12312')
        self.organization = Organization.objects.create(name ='organization test', owner=self.user, slug='org-test')
        self.membership = Membership.objects.create(user=self.user, organization = self.organization, control = 'supadm', is_active = True)
        self.project = Project.objects.create(name='project test', organization=self.organization, created_by = self.user)
        self.board = Board.objects.create(name='board1', project = self.project, position = 1)
        
class TaskViewsetTest(TaskTestBase):
    
# test for crud operations of taskviewset
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
        
        task = Task.objects.get()
        self.assertEqual(task.title, 'task test')
        self.assertEqual(task.created_by, self.user)
        self.assertEqual(Activity.objects.count(), 1)

    def test_list(self):
        Task.objects.create(title='Task1', description='list test', project=self.project, board=self.board, assignee=self.assignee, created_by=self.user, status='pending')
        response = self.client.get('/tasks/tasks/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), Task.objects.filter(project=self.project).count())

    def test_update(self):
        task = Task.objects.create(title = 'previous task', description = 'update test', project = self.project, board = self.board, assignee = self.assignee, created_by = self.user, status = 'pending')
        data = {
            'title': 'updated task',
            'description': 'updated description',
            'project': self.project.id,
            'board': self.board.id,
            'assignee': self.assignee.id,
            'status': 'done'
        }
        response = self.client.put(f'/tasks/tasks/{task.id}/', data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, 200)
        task.refresh_from_db()
        self.assertEqual(task.title, 'updated task')
        self.assertEqual(task.description, 'updated description')
        self.assertEqual(task.status, 'done')
        
    def test_delete(self):
        task = Task.objects.create(title='task delete', description='delete test', project=self.project, board=self.board, assignee=self.assignee, created_by=self.user, status='pending')
        response = self.client.delete(f'/tasks/tasks/{task.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Task.objects.filter(id=task.id).exists())
             
# custom actions tests for the taskviewset

    def test_give_task(self):
      task = Task.objects.create(title = 'task for giving', description = 'testing giving task action', project=self.project, board=self.board, assignee=None, created_by=self.user, status = 'pending')
      data = {'user_id': self.assignee.id}
      response = self.client.post(f'/tasks/tasks/{task.id}/task/', data, format='json')
      self.assertEqual(response.status_code, 200)
      
      task.refresh_from_db()
      self.assertEqual(task.assignee.id, self.assignee.id)
      self.assertEqual(response.data['msg'], 'task not given')
    
    def test_status(self):
      task = Task.objects.create(title = 'task for status', description = 'testing status action', project=self.project, board=self.board, assignee=self.assignee, created_by=self.user, status = 'pending')
      data = {'status': 'working'}
      response = self.client.post(f'/tasks/tasks/{task.id}/status/', data, format='json')
      self.assertEqual(response.status_code, 200)
    
      task.refresh_from_db()
      self.assertEqual(task.status, 'working')
      self.assertEqual(response.data['msg'], 'task is updated')
    
    def test_completed(self):
      task = Task.objects.create(title = 'task of completed', description = 'testing completed action', project=self.project, board=self.board, assignee=self.assignee, created_by=self.user, status = 'pending')
      response = self.client.post(f'/tasks/tasks/{task.id}/completed/', format='json')
      self.assertEqual(response.status_code, 200)
    
      task.refresh_from_db()
      self.assertEqual(task.status, 'done')
      self.assertEqual(response.data['msg'], 'task is completed')
      
    def test_comment(self):
      task = Task.objects.create(title = 'task of comment', description = 'testing comment action',  project=self.project, board=self.board, assignee=self.assignee, created_by=self.user, status = 'pending')
      data = {'content': 'test for comment'}
      response = self.client.post(f'/tasks/tasks/{task.id}/comment/', data, format='json')
      self.assertEqual(response.status_code, 200)
     
      task.refresh_from_db()
      self.assertEqual(task.comments.count(), 1)
      self.assertEqual(task.comments.first().content, 'test for comment')
      self.assertEqual(response.data['msg'], 'have some shame friend')

