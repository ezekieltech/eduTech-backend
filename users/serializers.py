from rest_framework import serializers
from users.models import CustomUser

from rest_framework_simplejwt.tokens import RefreshToken

class CustomUserSerializer(serializers.ModelSerializer):

    tokens = serializers.SerializerMethodField()
    profile_mentor  = serializers.PrimaryKeyRelatedField(read_only=True,)
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)


    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'role','password', 'password2','profile_mentor','tokens']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def get_tokens(self, CustomUser):
        """Get token pair for users

        Arguments:
            CustomUser {cls} -- the custom user model

        Returns:
            array -- An array of token
        """

        if self.context['request'].POST:
            refresh = RefreshToken.for_user(self.context['request'].user)
            data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
                }
            return data

    def save(self):
        """Over-riding the defaut save on serializers

        Raises:
            serializers.ValidationError: for password mismatch

        Returns:
            user object -- Sets the password and returns the user.
        """

        user = CustomUser(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            role=self.validated_data['role']
            )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Passwords must match'})

        user.set_password(password)
        user.save()

        return user
