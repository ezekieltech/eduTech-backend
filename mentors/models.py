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
                                related_name="mentor_profile")
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
