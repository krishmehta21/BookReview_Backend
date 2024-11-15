from rest_framework.test import APITestCase
from rest_framework import status

class BookIntegrationTestCase(APITestCase):
    def test_user_registration_and_book_creation(self):
        # Register a user
        user_data = {"username": "testuser", "password": "password123", "email": "test@example.com"}
        response = self.client.post("/api/auth/register/", user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Log in to get token
        response = self.client.post("/api/auth/token/", {"username": "testuser", "password": "password123"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

        # Create a book
        book_data = {
            "title": "Django for Beginners",
            "author": "William S. Vincent",
            "isbn": "1234567890",
            "genre": "Technology",
            "cover_image_url": "http://example.com/image.jpg"
        }
        response = self.client.post("/api/books/", book_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
