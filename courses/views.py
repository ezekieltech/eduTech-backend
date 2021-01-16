from rest_framework import viewsets
from courses.models import ClassCourse, ClassCourseLectures
from courses.serializers import ClassCourseSerializer, ClassCourseLecturesSerializers


class ClassCourseViewSet(viewsets.ModelViewSet):

    queryset = ClassCourse.objects.all()
    serializer_class = ClassCourseSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

class ClassCourseLecturesViewSet(viewsets.ModelViewSet):

    queryset = ClassCourseLectures.objects.all()
    serializer_class = ClassCourseLecturesSerializers
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
