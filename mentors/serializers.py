import jsons

from rest_framework import serializers
from mentors.models import MentorProfile

from users.serializers import CustomUserSerializer
from users.models import CustomUser

class MentorProfileSerializer(serializers.ModelSerializer):

    users = serializers.SerializerMethodField()

    def get_users(self, MentorProfile):
        users = CustomUser.objects.filter(
            role='Mentor').values(
            'username', 'email')
        users_to_json = jsons.dump(
            users)  # gets the queryset serlizable
        return users

    class Meta:
        model = MentorProfile
        fields = ['users', 'first_name', 'last_name', 'bio']