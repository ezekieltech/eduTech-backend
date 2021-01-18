from rest_framework import viewsets
from rest_framework import permissions

from profiles.models import MentorProfile, MenteeProfile, EduconsultantProfile
from profiles.serializers import MentorProfileSerializer, MenteeProfileSerializer, EduconsultantProfileSerializer


class MentorProfileViewSet(viewsets.ModelViewSet):

    queryset = MentorProfile.objects.all()
    serializer_class = MentorProfileSerializer
    permission_classes = [permissions.IsAuthenticated,]

class MenteeProfileViewSet(viewsets.ModelViewSet):

    queryset = MenteeProfile.objects.all()
    serializer_class = MenteeProfileSerializer
    permission_classes = [permissions.IsAuthenticated,]

class EduconsultantProfileViewSet(viewsets.ModelViewSet):

    queryset = EduconsultantProfile.objects.all()
    serializer_class = EduconsultantProfileSerializer
    permission_classes = [permissions.IsAuthenticated,]
