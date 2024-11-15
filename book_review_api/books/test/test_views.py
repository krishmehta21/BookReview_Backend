from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from books.models import Book

class BookViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.login(username="testuser", password="password123")
        self.book_data = {
            "title": "Django for Beginners",
            "author": "William S. Vincent",
            "isbn": "1234567890",
            "genre": "Technology",
            "cover_image_url": "http://example.com/image.jpg"
        }
        self.book = Book.objects.create(**self.book_data)

    def test_create_book(self):
        response = self.client.post("/api/books/", self.book_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_books(self):
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Django for Beginners")
