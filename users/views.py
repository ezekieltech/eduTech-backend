from rest_framework import viewsets
from users.models import CustomUser
from users.serializers import CustomUserSerializer

from rest_framework import permissions
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class CustomUserViewSet(viewsets.ModelViewSet):
    
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
