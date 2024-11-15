from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),  # Authentication URLs
    path('', lambda request: HttpResponseRedirect('/api/auth/')),  # Redirect root to /api/auth/
    path('api/', include('books.urls')),
    path('api/', include('reviews.urls')),
]
