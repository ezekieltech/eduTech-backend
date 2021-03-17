from django.contrib import admin

from .models import ClassCourse, ClassCourseLectures, LecturesFiles
# Register your models here.

admin.site.register(ClassCourse)
admin.site.register(ClassCourseLectures)
admin.site.register(LecturesFiles)
