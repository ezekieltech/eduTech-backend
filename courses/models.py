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
    course_creator      = models.ForeignKey(MentorProfile, on_delete=models.CASCADE,
                                related_name='course_creator', null=True, default=None)
    name                =   models.CharField(max_length=30, unique=True,)
    short_description   = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name +',' + str(self.id)

class ClassCourseLectures(models.Model):
    lectures            = models.ForeignKey('ClassCourse',
                                on_delete=models.CASCADE,
                                related_name="classcourse_lectures", null=True,blank=True)
    title               =   models.CharField(max_length=30)
    short_description   = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title +',' + str(self.id)


class LecturesFiles (models.Model):
    files_lectures      =   models.ManyToManyField(ClassCourseLectures, 
                                related_name='files_of_ClassCourseLectures',)
    video_file          =   models.FileField(upload_to='lecture_video_files',blank=True,null=True)
    document_file       =   models.FileField(upload_to='lecture_document_files',blank=True,null=True)
    text_content        =   models.TextField(blank=True,null=True)

    def __str__(self):
        return self.text_content + ',' + str(self.id)