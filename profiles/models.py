from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


class MentorProfile(models.Model):
    """A django model for mentor profile

    Arguments:
        models {Generic Model} -- A generic model class
    """
    user            = models.OneToOneField(settings.AUTH_USER_MODEL,
                                limit_choices_to={'role': 'Mentor'},
                                on_delete=models.CASCADE,
                                related_name="profile_mentor")
    first_name      = models.CharField(max_length=30, blank=True, null=True)
    last_name       = models.CharField(max_length=30,blank=True, null=True)
    bio             = models.TextField(null=True, blank=True)
    gender          = models.CharField(max_length=10, null=True, blank=True)
    # message = models.ManyToManyField(
    #     'patients.Messages', blank=True)
    # assigned_patients = models.ManyToManyField(
    #     'patients.PatientProfile', blank=True)
    # list_of_classes = models.ManyToManyField(
    #     'ExpertClass', blank=True)

    def __str__(self):
        return self.user.username

class MenteeProfile(models.Model):
    """A django model for mentor profile

    Arguments:
        models {Generic Model} -- A generic model class
    """
    user            = models.OneToOneField(settings.AUTH_USER_MODEL,
                                limit_choices_to={'role': 'Mentee'},
                                on_delete=models.CASCADE,
                                related_name="profile_mentee")
    first_name      = models.CharField(max_length=30, blank=True, null=True)
    last_name       = models.CharField(max_length=30,blank=True, null=True)
    bio             = models.TextField(null=True, blank=True)
    gender          = models.CharField(max_length=10, null=True, blank=True)
    # message = models.ManyToManyField(
    #     'patients.Messages', blank=True)
    # assigned_patients = models.ManyToManyField(
    #     'patients.PatientProfile', blank=True)
    # list_of_classes = models.ManyToManyField(
    #     'ExpertClass', blank=True)

    def __str__(self):
        return self.user.username


class EduconsultantProfile(models.Model):
    """A django model for mentor profile

    Arguments:
        models {Generic Model} -- A generic model class
    """
    user            = models.OneToOneField(settings.AUTH_USER_MODEL,
                                limit_choices_to={'role': 'Edu-Consultant'},
                                on_delete=models.CASCADE,
                                related_name="profile_educonsultant")
    first_name      = models.CharField(max_length=30, blank=True, null=True)
    last_name       = models.CharField(max_length=30,blank=True, null=True)
    bio             = models.TextField(null=True, blank=True)
    gender          = models.CharField(max_length=10, null=True, blank=True)
    # message = models.ManyToManyField(
    #     'patients.Messages', blank=True)
    # assigned_patients = models.ManyToManyField(
    #     'patients.PatientProfile', blank=True)
    # list_of_classes = models.ManyToManyField(
    #     'ExpertClass', blank=True)

    def __str__(self):
        return self.user.username

