from django.urls import path, include
from rest_framework.routers import DefaultRouter
from catalogue import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'books', views.BookViewset)
router.register(r'authors', views.AuthorViewset)
router.register(r'renew', views.BookInstanceViewSet)

urlpatterns = [
    # path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    path('', include(router.urls)),
]

