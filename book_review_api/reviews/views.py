# reviews/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        book_id = self.request.query_params.get('book', None)
        if book_id:
            return Review.objects.filter(book_id=book_id)
        return Review.objects.all()

    @action(detail=True, methods=['post'])
    def add_review(self, request, pk=None):
        book = self.get_object()
        rating = request.data.get('rating')
        content = request.data.get('content')
        user = request.user

        # Check if the user has already reviewed the book
        if Review.objects.filter(book=book, user=user).exists():
            return Response({"message": "You have already reviewed this book."}, status=400)

        review = Review.objects.create(book=book, user=user, rating=rating, content=content)
        return Response({"message": "Review added successfully!"}, status=201)
