import jsons

from rest_framework import serializers

from profiles.models import MentorProfile, MenteeProfile, EduconsultantProfile
from users.models import CustomUser
from courses.models import ClassCourse

from users.serializers import CustomUserSerializer




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

    # mentor_courses = ClassCourseRelatedField(
    #     queryset=ClassCourse.objects.all(),
    #     many=True
    # )

    classcourse_mentor = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    mentee_mentor        = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    users = serializers.SerializerMethodField()

    def get_users(self, MentorProfile):
        users = CustomUser.objects.filter(
            role='Mentor').values(
            'username', 'email','role')
        users_to_json = jsons.dump(
            users)  # gets the queryset serlizable
        return users

    class Meta:
        model = MentorProfile
        fields = ['users', 'first_name', 'last_name', 'bio','classcourse_mentor','mentee_mentor']


class MenteeProfileSerializer(serializers.ModelSerializer):


    classcourse_mentee        = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    users = serializers.SerializerMethodField()

    def get_users(self, MentorProfile):
        users = CustomUser.objects.filter(
            role='Mentee').values(
            'username', 'email','role')
        users_to_json = jsons.dump(
            users)  # gets the queryset serlizable
        return users

    class Meta:
        model = MenteeProfile
        fields = ['users', 'first_name', 'last_name', 'bio','my_mentor','classcourse_mentee',]


class EduconsultantProfileSerializer(serializers.ModelSerializer):

    users = serializers.SerializerMethodField()

    def get_users(self, MentorProfile):
        users = CustomUser.objects.filter(
            role='Edu-Consultant').values(
            'username', 'email','role')
        users_to_json = jsons.dump(
            users)  # gets the queryset serlizable
        return users

    class Meta:
        model = EduconsultantProfile
        fields = ['users', 'first_name', 'last_name', 'bio']