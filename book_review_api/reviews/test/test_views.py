from rest_framework.test import APITestCase
from rest_framework import status
from reviews.models import Review
from books.models import Book
from django.contrib.auth.models import User

class ReviewViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.book = Book.objects.create(
            title="Django for Beginners",
            author="William S. Vincent",
            isbn="1234567890",
            genre="Technology",
            cover_image_url="http://example.com/image.jpg"
        )
        self.review_data = {
            "book": self.book.id,
            "rating": 5,
            "text": "Excellent book!"
        }

        self.client.login(username="testuser", password="password123")

    def test_create_review(self):
        response = self.client.post(f"/api/books/{self.book.id}/reviews/", self.review_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_reviews(self):
        Review.objects.create(book=self.book, user=self.user, rating=4, text="Great read!")
        response = self.client.get(f"/api/books/{self.book.id}/reviews/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["text"], "Great read!")
