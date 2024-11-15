from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class UserViewSetTestCase(APITestCase):
    def test_user_registration(self):
        user_data = {
            "username": "testuser",
            "password": "password123",
            "email": "test@example.com"
        }
        response = self.client.post("/api/auth/register/", user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login(self):
        User.objects.create_user(username="testuser", password="password123")
        login_data = {
            "username": "testuser",
            "password": "password123"
        }
        response = self.client.post("/api/auth/token/", login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
