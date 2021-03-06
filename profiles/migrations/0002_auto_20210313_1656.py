# Generated by Django 3.1.5 on 2021-03-13 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='mentorprofile',
            name='user',
            field=models.OneToOneField(limit_choices_to={'role': 'Mentor'}, on_delete=django.db.models.deletion.CASCADE, related_name='profile_mentor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='menteeprofile',
            name='user',
            field=models.OneToOneField(limit_choices_to={'role': 'Mentee'}, on_delete=django.db.models.deletion.CASCADE, related_name='profile_mentee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='educonsultantprofile',
            name='user',
            field=models.OneToOneField(limit_choices_to={'role': 'Edu-Consultant'}, on_delete=django.db.models.deletion.CASCADE, related_name='profile_educonsultant', to=settings.AUTH_USER_MODEL),
        ),
    ]
