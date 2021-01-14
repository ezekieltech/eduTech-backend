from rest_framework import viewsets
from profiles.models import MentorProfile, MenteeProfile, EduconsultantProfile
from profiles.serializers import MentorProfileSerializer, MenteeProfileSerializer, EduconsultantProfileSerializer


class MentorProfileViewSet(viewsets.ModelViewSet):

    queryset = MentorProfile.objects.all()
    serializer_class = MentorProfileSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

class MenteeProfileViewSet(viewsets.ModelViewSet):

    queryset = MenteeProfile.objects.all()
    serializer_class = MenteeProfileSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

class EduconsultantProfileViewSet(viewsets.ModelViewSet):

    queryset = EduconsultantProfile.objects.all()
    serializer_class = EduconsultantProfileSerializer