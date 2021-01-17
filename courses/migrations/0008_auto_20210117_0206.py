# Generated by Django 3.1.5 on 2021-01-17 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_lecturesfiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturesfiles',
            name='document_file',
            field=models.FileField(blank=True, null=True, upload_to='lecture_document_files'),
        ),
        migrations.AlterField(
            model_name='lecturesfiles',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='lecture_video_files'),
        ),
    ]