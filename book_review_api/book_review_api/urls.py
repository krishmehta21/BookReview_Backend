from django.contrib import admin
from django.urls import path, include, re_path
from django.shortcuts import redirect
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Book Review API",
        default_version='v1',
        description="API documentation for the Book Review application",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="21mehtak@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include('books.urls')),
    path('api/', include('reviews.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^$', lambda request: redirect('schema-swagger-ui', permanent=True)),  # Redirect to Swagger UI
]
