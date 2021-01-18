from rest_framework import status, viewsets
from rest_framework.parsers import FileUploadParser
from rest_framework import permissions
from rest_framework.response import Response

from courses.permissions import IsOwnerOrReadOnly

from courses.models import ClassCourse, ClassCourseLectures, LecturesFiles
from courses.serializers import ClassCourseSerializer, ClassCourseLecturesSerializers, LecturesFilesSerializers


class ClassCourseViewSet(viewsets.ModelViewSet):

    queryset = ClassCourse.objects.all()
    serializer_class = ClassCourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        if hasattr(user, 'profile_mentor'):
            user_profile = user.profile_mentor
            serializer.save(course_creator=user_profile)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )

class ClassCourseLecturesViewSet(viewsets.ModelViewSet):

    queryset = ClassCourseLectures.objects.all()
    serializer_class = ClassCourseLecturesSerializers
    permission_classes = [permissions.IsAuthenticated,]

class LecturesFilesViewSet(viewsets.ModelViewSet):
    parser_class = (FileUploadParser,)
    queryset = LecturesFiles.objects.all()
    serializer_class = LecturesFilesSerializers
    permission_classes = [permissions.IsAuthenticated,]
