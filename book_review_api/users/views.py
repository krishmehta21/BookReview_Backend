from rest_framework import status, generics, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import AllowAny

# Serializer for User Registration
class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer to handle user registration with secure password hashing.
    """
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Hash the password and create a new user.
        """
        validated_data['password'] = make_password(validated_data['password'])
        return User.objects.create(**validated_data)


# API View for Default Authentication Information
class DefaultAuthView(APIView):
    """
    Provides an overview of the API's authentication and main features.
    """
    permission_classes = [AllowAny]

    def get(self, request):
        """
        Returns a description of the API's endpoints.
        """
        return Response(
            {
                "message": "Welcome to the Book Review API! Below are the available endpoints for authentication, book management, and reviews:",
                "endpoints": {
                    "Authentication": {
                        "Register": {
                            "url": "/api/auth/register/",
                            "description": "Create a new user account by providing a username, password, and email."
                        },
                        "Login": {
                            "url": "/api/auth/token/",
                            "description": "Obtain a JWT token by providing a username and password. Use this token to authenticate future requests."
                        },
                        "Refresh Token": {
                            "url": "/api/auth/token/refresh/",
                            "description": "Refresh your JWT token to keep your session active."
                        }
                    },
                    "Book Management": {
                        "Add Book": {
                            "url": "/api/books/",
                            "method": "POST",
                            "description": "Add a new book by providing details such as title, author, ISBN, genre, and cover image URL."
                        },
                        "Retrieve Books": {
                            "url": "/api/books/",
                            "method": "GET",
                            "description": "Retrieve a list of all books. Supports search, sorting, filtering, and pagination."
                        },
                        "Retrieve Single Book": {
                            "url": "/api/books/<book_id>/",
                            "method": "GET",
                            "description": "Retrieve details of a single book using its ID."
                        },
                        "Update Book": {
                            "url": "/api/books/<book_id>/",
                            "method": "PUT",
                            "description": "Update the information of an existing book."
                        },
                        "Delete Book": {
                            "url": "/api/books/<book_id>/",
                            "method": "DELETE",
                            "description": "Delete a book by its ID."
                        }
                    },
                    "Reviews": {
                        "Add Review": {
                            "url": "/api/books/<book_id>/reviews/",
                            "method": "POST",
                            "description": "Add a review for a specific book, including a rating (1-5 stars) and text content."
                        },
                        "Retrieve Reviews": {
                            "url": "/api/books/<book_id>/reviews/",
                            "method": "GET",
                            "description": "Retrieve all reviews for a specific book. Supports pagination."
                        },
                        "Edit Review": {
                            "url": "/api/books/<book_id>/reviews/<review_id>/",
                            "method": "PUT",
                            "description": "Edit an existing review. Only the owner of the review can perform this action."
                        },
                        "Delete Review": {
                            "url": "/api/books/<book_id>/reviews/<review_id>/",
                            "method": "DELETE",
                            "description": "Delete an existing review. Only the owner of the review can perform this action."
                        }
                    },
                    "Complex Logic": {
                        "Recommendation System": {
                            "url": "/api/books/recommendations/",
                            "method": "GET",
                            "description": "Retrieve a list of recommended books based on genre, author, or user rating patterns."
                        },
                        "Sorting and Filtering": {
                            "url": "/api/books/",
                            "method": "GET",
                            "description": "Sort and filter books by title, author, average rating, genre, or date added. Combine multiple filters for custom results."
                        },
                        "Pagination": {
                            "url": "/api/books/ and /api/books/<book_id>/reviews/",
                            "method": "GET",
                            "description": "Paginate lists of books or reviews to display a limited number of items per page."
                        }
                    }
                },
                "notes": "Use the endpoints above to authenticate, manage books, and interact with reviews. Make sure to include a valid JWT token in the Authorization header for protected routes."
            },
            status=status.HTTP_200_OK
        )


# View for User Registration
class RegisterView(generics.CreateAPIView):
    """
    Handles user registration by creating a new user in the database.
    """
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        """
        Handles the creation of a new user.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User registered successfully"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
