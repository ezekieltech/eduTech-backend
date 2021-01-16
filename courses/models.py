from django.db import models
from django.conf import settings

from profiles.models import MentorProfile, MenteeProfile, EduconsultantProfile

# Create your models here.
class ClassCourse(models.Model):
    teacher             = models.ManyToManyField(MentorProfile,
                                related_name="classcourse_mentor")
    student             = models.ManyToManyField(MenteeProfile,                                
                                related_name="classcourse_mentee")
    consultant          = models.ManyToManyField(EduconsultantProfile,                                
                                related_name="classcourse_educonsultant")
    name                =   models.CharField(max_length=30, unique=True,)
    short_description   = models.CharField(max_length=200, blank=True, null=True)


class ClassCourseLectures(models.Model):
    lectures            = models.ForeignKey('ClassCourse',
                                on_delete=models.CASCADE,
                                related_name="classcourse_lectures", null=True,blank=True)
    title               =   models.CharField(max_length=30)
    short_description   = models.CharField(max_length=200, blank=True, null=True)