from rest_framework import serializers
from users.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):


    profile_mentor  = serializers.PrimaryKeyRelatedField(read_only=True,)
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)


    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'role','password', 'password2','profile_mentor',]
        extra_kwargs = {
            'password': {'write_only': True}
        }

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
