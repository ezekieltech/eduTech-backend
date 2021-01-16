# Generated by Django 3.1.5 on 2021-01-15 13:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0003_auto_20210114_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='classcourse',
            name='teacher',
            field=models.ManyToManyField(limit_choices_to={'role': 'Mentor'}, related_name='classcourse_mentor', to=settings.AUTH_USER_MODEL),
        ),
    ]
