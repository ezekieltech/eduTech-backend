from django.urls import path, include
from rest_framework.routers import DefaultRouter
from courses import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'classcourses', views.ClassCourseViewSet)
router.register(r'lectures', views.ClassCourseLecturesViewSet)
router.register(r'fileslectures', views.LecturesFilesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

