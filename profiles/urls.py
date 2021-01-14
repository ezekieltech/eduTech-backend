from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'mentors', views.MentorProfileViewSet)
router.register(r'mentees', views.MenteeProfileViewSet)
router.register(r'edu-consultants', views.EduconsultantProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]