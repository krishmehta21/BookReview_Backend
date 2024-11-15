from django.test import TestCase
from reviews.models import Review
from books.models import Book
from django.contrib.auth.models import User
from reviews.serializers import ReviewSerializer

class ReviewSerializerTestCase(TestCase):
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
            "user": self.user.id,
            "rating": 5,
            "text": "Excellent book!"
        }
        self.review = Review.objects.create(**self.review_data)

    def test_review_serializer_contains_correct_fields(self):
        serializer = ReviewSerializer(instance=self.review)
        self.assertEqual(set(serializer.data.keys()), {"id", "book", "user", "rating", "text", "created_at"})

    def test_review_serializer_validation(self):
        serializer = ReviewSerializer(data=self.review_data)
        self.assertTrue(serializer.is_valid())
