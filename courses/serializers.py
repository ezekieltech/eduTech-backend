from rest_framework import serializers
from courses.models import ClassCourse, ClassCourseLectures, LecturesFiles

class ClassCourseSerializer(serializers.ModelSerializer):

    classcourse_lectures = serializers.StringRelatedField(many=True)
    teacher = serializers.StringRelatedField(many=True)
    course_creator = serializers.ReadOnlyField(source='course_creator.username') # same as CharField(read_only=True)

    class Meta:
        model = ClassCourse
        fields = ['course_creator','name','classcourse_lectures','teacher','consultant', 'short_description']

class ClassCourseLecturesSerializers(serializers.ModelSerializer):

    files_of_ClassCourseLectures = serializers.StringRelatedField(many=True)

    class Meta:
        model = ClassCourseLectures
        fields = ['id', 'title', 'short_description', 'lectures', 'files_of_ClassCourseLectures']


class LecturesFilesSerializers(serializers.ModelSerializer):
    class Meta:
        model = LecturesFiles
        fields  = '__all__'
