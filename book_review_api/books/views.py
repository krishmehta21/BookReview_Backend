from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Q
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['genre', 'author', 'isbn']
    ordering_fields = ['title', 'author', 'average_rating', 'date_added']
    ordering = ['title']  # Default ordering by title

    def get_queryset(self):
        queryset = Book.objects.all()
        title = self.request.query_params.get('title', None)
        author = self.request.query_params.get('author', None)
        isbn = self.request.query_params.get('isbn', None)
        
        if title:
            queryset = queryset.filter(title__icontains=title)
        if author:
            queryset = queryset.filter(author__icontains=author)
        if isbn:
            queryset = queryset.filter(isbn=isbn)
        
        return queryset

    @action(detail=True, methods=['get'])
    def recommend(self, request, pk=None):
        # Get the current book
        book = self.get_object()
        genre = book.genre
        author = book.author

        # Recommend books with the same genre or author
        recommended_books = Book.objects.filter(
            Q(genre=genre) | Q(author=author)
        ).exclude(id=book.id)  # Exclude the current book from recommendations

        serializer = BookSerializer(recommended_books, many=True)
        return Response(serializer.data)
