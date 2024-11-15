from django.test import TestCase
from books.models import Book
from books.serializers import BookSerializer

class BookSerializerTestCase(TestCase):
    def setUp(self):
        self.book_data = {
            "title": "Django for Beginners",
            "author": "William S. Vincent",
            "isbn": "1234567890",
            "genre": "Technology",
            "cover_image_url": "http://example.com/image.jpg"
        }
        self.book = Book.objects.create(**self.book_data)

    def test_book_serializer_contains_correct_fields(self):
        serializer = BookSerializer(instance=self.book)
        self.assertEqual(set(serializer.data.keys()), {"id", "title", "author", "isbn", "genre", "cover_image_url"})

    def test_book_serializer_validation(self):
        serializer = BookSerializer(data=self.book_data)
        self.assertTrue(serializer.is_valid())
