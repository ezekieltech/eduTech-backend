from rest_framework import serializers
from courses.models import ClassCourse, ClassCourseLectures

class ClassCourseSerializer(serializers.ModelSerializer):

    classcourse_lectures = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = ClassCourse
        fields = ['name','classcourse_lectures','teacher','consultant']

class ClassCourseLecturesSerializers(serializers.ModelSerializer):

    class Meta:
        model = ClassCourseLectures
        fields = ['title','lectures']
