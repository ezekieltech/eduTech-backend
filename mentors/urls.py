from django.urls import path, include
from rest_framework.routers import DefaultRouter
from mentors import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'mentors', views.MentorProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]