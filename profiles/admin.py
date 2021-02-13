from django.contrib import admin

from .models import MenteeProfile, MentorProfile, EduconsultantProfile

# Register your models here.

admin.site.register(MenteeProfile)

admin.site.register(MentorProfile)

admin.site.register(EduconsultantProfile)
