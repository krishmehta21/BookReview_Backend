# **Book Review API**

## **Overview**
The **Book Review API** is a feature-rich backend application built with the Django REST framework. It enables users to register, authenticate, manage books, write reviews, and receive personalized book recommendations. This project demonstrates advanced skills in Django development, RESTful API design, and secure coding practices, focusing on scalability, maintainability, and extensibility.

---

## **Tech Stack**
- **Backend Framework**: Python with Django
- **API Framework**: Django REST framework (DRF)
- **Database**: PostgreSQL
- **ORM**: Django ORM
- **Authentication**: JWT via `djangorestframework-simplejwt`
- **API Documentation**: Swagger UI using `drf-yasg`

---

## **Features**

### **1. User Authentication**
- Secure registration and login using JWT tokens.
- Encrypted password storage with Django’s built-in hashing mechanisms.
- Token refresh for seamless session management.

### **2. Book Management**
- Add, update, retrieve, and delete books with fields like:
  - Title, Author, ISBN, Genre, and Cover Image URL.
- Search functionality to filter books by title, author, or ISBN.

### **3. Reviews**
- Add, edit, or delete reviews for any book.
- Include a star rating (1-5) and optional comments.
- Automatically calculate and display average ratings for books.

### **4. Advanced Features**
- **Recommendation System**: Suggest books based on genres, authors, or user behavior.
- **Sorting & Filtering**: Organize books by title, author, ratings, and genres.
- **Pagination**: Handle large datasets efficiently for books and reviews.

### **5. Interactive API Documentation**
- Fully interactive Swagger documentation available at `/swagger/`.

---

## **Setup Instructions**

### **Prerequisites**
Ensure the following are installed on your system:
- **Python** (3.10 or later)
- **PostgreSQL** (12 or later)
- **Git**
- **pip** (Python package manager)

---

### **Installation**

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd book_review_api
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Database**
   - Create a PostgreSQL database for the project.
   - Update the database settings in `book_review/settings.py`:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': '<your-database-name>',
             'USER': '<your-database-username>',
             'PASSWORD': '<your-database-password>',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

5. **Apply Database Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

8. **Access API Documentation**
   Open your browser and visit:
   ```
   http://127.0.0.1:8000/swagger/
   ```

---

## **Testing**

Run all tests to ensure the application is functioning correctly:
```bash
python manage.py test
```

---

## **API Endpoints**

### **Authentication**
| Endpoint                      | Method | Description                          |
|-------------------------------|--------|--------------------------------------|
| `/api/auth/register/`         | POST   | Register a new user.                |
| `/api/auth/token/`            | POST   | Obtain a JWT token.                 |
| `/api/auth/token/refresh/`    | POST   | Refresh an existing JWT token.      |

### **Book Management**
| Endpoint                       | Method | Description                          |
|--------------------------------|--------|--------------------------------------|
| `/api/books/`                  | GET    | Retrieve all books.                 |
| `/api/books/<id>/`             | GET    | Retrieve a specific book.           |
| `/api/books/`                  | POST   | Add a new book.                     |
| `/api/books/<id>/`             | PUT    | Update book details.                |
| `/api/books/<id>/`             | DELETE | Delete a book.                      |

### **Reviews**
| Endpoint                              | Method | Description                          |
|---------------------------------------|--------|--------------------------------------|
| `/api/books/<book_id>/reviews/`       | GET    | Retrieve all reviews for a book.     |
| `/api/books/<book_id>/reviews/`       | POST   | Add a new review for a book.         |
| `/api/books/<book_id>/reviews/<id>/`  | PUT    | Edit a review.                       |
| `/api/books/<book_id>/reviews/<id>/`  | DELETE | Delete a review.                     |

### **Advanced Features**
| Endpoint                              | Method | Description                          |
|---------------------------------------|--------|--------------------------------------|
| `/api/books/recommendations/`         | GET    | Fetch personalized book recommendations. |
| `/api/books/`                         | GET    | Sort or filter books based on criteria.|

---

## **Security Highlights**
- **Password Encryption**: Secure hashing using Django’s PBKDF2 algorithm.
- **JWT Authentication**: Protect routes and maintain secure sessions.
- **Input Validation**: Prevent SQL injection and cross-site scripting (XSS) attacks.

---

## **Documentation**
- Interactive Swagger documentation is accessible at:
  ```
  http://127.0.0.1:8000/swagger/
  ```
- Detailed API schema provides endpoint descriptions and usage examples.

---

## **Code Quality**
- Fully adheres to **PEP 8** coding standards.
- Includes unit and integration tests for robust functionality.
- Extensible design for future enhancements.

---

## **Future Enhancements**
- Implement AI/ML-driven recommendations.
- Add advanced search filters (e.g., publication year, publisher).
- Improve user analytics with detailed reports.

---

## **Contributing**
Contributions are welcome! Please fork the repository and submit a pull request with your proposed changes.

Feel free to explore and extend this project! 🚀