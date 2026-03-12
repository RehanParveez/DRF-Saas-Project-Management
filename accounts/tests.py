from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model

# Create your tests here.
class ParentTest(APITestCase):
    def setUp(self):
      self.client = APIClient()
      User = get_user_model()
      self.user = User.objects.create_user(username = 'usertest', email = 'usertest@gmail.com', password = 'pass12312')
      self.client.force_authenticate(user=self.user)
        
class AuthTest(ParentTest):
    def test_user(self):
       self.assertEqual(self.user.username, 'usertest')
        