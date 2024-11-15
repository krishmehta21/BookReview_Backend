# books/models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    genre = models.CharField(max_length=100)
    cover_image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
