# Generated by Django 3.1.5 on 2021-03-17 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210313_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('Mentor', 'Mentor'), ('Mentee', 'Mentee'), ('Edu-Consultant', 'Edu-Consultant')], default='Mentor', max_length=20),
        ),
    ]
