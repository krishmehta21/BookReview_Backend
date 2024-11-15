from django.test import TestCase
from books.models import Book

class BookModelTestCase(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Django for Beginners",
            author="William S. Vincent",
            isbn="1234567890",
            genre="Technology",
            cover_image_url="http://example.com/image.jpg"
        )

    def test_book_creation(self):
        self.assertEqual(self.book.title, "Django for Beginners")
        self.assertEqual(str(self.book), "Django for Beginners")  # Assuming the __str__ method is implemented.
