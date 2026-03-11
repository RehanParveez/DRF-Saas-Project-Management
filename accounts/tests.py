from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

# Create your tests here.
class ParentTest(APITestCase):
    def setUp(self):
      self.client = APIClient()
      User = get_user_model()
      self.user = User.objects.create_user(username = 'usertest', email = 'usertestgmail.com', password = 'pass12312')
      refresh = RefreshToken.for_user(self.user)
      self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        
class AuthTest(ParentTest):
    def test_user(self):
       self.assertEqual(self.user.username, 'usertest')
        