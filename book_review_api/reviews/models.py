# reviews/models.py
from django.db import models
from django.contrib.auth.models import User
from books.models import Book

class Review(models.Model):
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')])
    content = models.TextField()

    def __str__(self):
        return f'Review for {self.book.title} by {self.user.username}'
