from rest_framework import serializers

from profiles.models import MentorProfile, MenteeProfile, EduconsultantProfile
from users.models import CustomUser
from courses.models import ClassCourse


class ClassCourseRelatedField(serializers.RelatedField):
    """A serliazer class of type related field,
    overides how the output ClassCourse in the
    serializers

    Arguments:
        serializers {RelatedField} --
        for defining how the output ClassCourse
    """

    # defines how the object is displayed
    def display_value(self, instance):
        return instance

    # defines how the object Genre is displayed in the output (JSON or XML)
    def to_representation(self, value):
        return str(value)

    # gets an object Message for the given value
    def to_internal_value(self, data):
        return ClassCourse.objects.get(name=data)

class MentorProfileSerializer(serializers.ModelSerializer):

    classcourse_mentor = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # profile_mentor        = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    course_creator      =  serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = MentorProfile
        fields = ['first_name', 'last_name', 'bio', 'classcourse_mentor','course_creator']


class MenteeProfileSerializer(serializers.ModelSerializer):


    classcourse_mentee        = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = MenteeProfile
        fields = ['first_name', 'last_name', 'bio','classcourse_mentee',]


class EduconsultantProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = EduconsultantProfile
        fields = ['first_name', 'last_name', 'bio']