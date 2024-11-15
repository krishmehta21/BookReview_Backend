from django.test import TestCase
from django.contrib.auth.models import User
from users.serializers import RegisterSerializer

class RegisterSerializerTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            "username": "testuser",
            "password": "password123",
            "email": "test@example.com"
        }

    def test_registration_serializer_validation(self):
        serializer = RegisterSerializer(data=self.user_data)
        self.assertTrue(serializer.is_valid())
