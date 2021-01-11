from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.CustomUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]