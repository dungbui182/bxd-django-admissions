# Generated by Django 5.0.1 on 2024-05-15 15:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admissions', '0010_alter_comments_time_alter_faculty_introduction_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 15, 22, 27, 38, 449269)),
        ),
        migrations.AlterField(
            model_name='livestream',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 15, 22, 27, 38, 449269)),
        ),
        migrations.AlterField(
            model_name='questions',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 15, 22, 27, 38, 449269)),
        ),
    ]