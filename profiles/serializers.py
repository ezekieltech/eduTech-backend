import jsons

from rest_framework import serializers
from profiles.models import MentorProfile, MenteeProfile, EduconsultantProfile

from users.serializers import CustomUserSerializer
from users.models import CustomUser

class MentorProfileSerializer(serializers.ModelSerializer):

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
        fields = ['users', 'first_name', 'last_name', 'bio']


class MenteeProfileSerializer(serializers.ModelSerializer):

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
        fields = ['users', 'first_name', 'last_name', 'bio']


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