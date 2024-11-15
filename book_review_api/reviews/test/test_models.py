from django.test import TestCase
from reviews.models import Review
from books.models import Book
from django.contrib.auth.models import User

class ReviewModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.book = Book.objects.create(
            title="Django for Beginners",
            author="William S. Vincent",
            isbn="1234567890",
            genre="Technology",
            cover_image_url="http://example.com/image.jpg"
        )
        self.review = Review.objects.create(
            book=self.book,
            user=self.user,
            rating=5,
            text="Excellent book!"
        )

    def test_review_creation(self):
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(str(self.review), f"Review by {self.user.username} on {self.book.title}")
