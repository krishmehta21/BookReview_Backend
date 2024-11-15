from django.test import TestCase
from django.contrib.auth.models import User

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")

    def test_user_creation(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertTrue(self.user.check_password("password123"))
