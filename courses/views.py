from rest_framework import viewsets
from rest_framework.parsers import FileUploadParser

from courses.models import ClassCourse, ClassCourseLectures, LecturesFiles
from courses.serializers import ClassCourseSerializer, ClassCourseLecturesSerializers, LecturesFilesSerializers


class ClassCourseViewSet(viewsets.ModelViewSet):

    queryset = ClassCourse.objects.all()
    serializer_class = ClassCourseSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

class ClassCourseLecturesViewSet(viewsets.ModelViewSet):

    queryset = ClassCourseLectures.objects.all()
    serializer_class = ClassCourseLecturesSerializers
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

class LecturesFilesViewSet(viewsets.ModelViewSet):
    parser_class = (FileUploadParser,)
    queryset = LecturesFiles.objects.all()
    serializer_class = LecturesFilesSerializers
