# Generated by Django 3.1.5 on 2021-03-13 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classcourse',
            name='consultant',
            field=models.ManyToManyField(related_name='classcourse_educonsultant', to='profiles.EduconsultantProfile'),
        ),
        migrations.AddField(
            model_name='classcourse',
            name='course_creator',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_creator', to='profiles.mentorprofile'),
        ),
        migrations.AddField(
            model_name='classcourse',
            name='student',
            field=models.ManyToManyField(related_name='classcourse_mentee', to='profiles.MenteeProfile'),
        ),
        migrations.AddField(
            model_name='classcourse',
            name='teacher',
            field=models.ManyToManyField(related_name='classcourse_mentor', to='profiles.MentorProfile'),
        ),
    ]
