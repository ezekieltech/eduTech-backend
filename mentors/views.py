from rest_framework import viewsets
from mentors.models import MentorProfile
from mentors.serializers import MentorProfileSerializer


class MentorProfileViewSet(viewsets.ModelViewSet):

    queryset = MentorProfile.objects.all()
    serializer_class = MentorProfileSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,]