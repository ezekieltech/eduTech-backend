from rest_framework import viewsets
from users.models import CustomUser
from users.serializers import CustomUserSerializer

from rest_framework.permissions import (
    AllowAny,
)

from rest_framework import permissions

class CustomUserViewSet(viewsets.ModelViewSet):
    
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = [permissions.IsAuthenticated,]
    http_method_names = ['post','get']
