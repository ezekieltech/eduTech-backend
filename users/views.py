from rest_framework import viewsets
from users.models import CustomUser
from users.serializers import CustomUserSerializer, CustomTokenObtainPairSerializer

from rest_framework_simplejwt.views import TokenObtainPairView


from rest_framework.permissions import (
    AllowAny,
)

from rest_framework import permissions

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    http_method_names = ['post']

class CustomUserViewSet(viewsets.ModelViewSet):
    
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = [permissions.IsAuthenticated,]
    http_method_names = ['get','post']
