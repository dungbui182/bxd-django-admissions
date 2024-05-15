# Generated by Django 5.0.1 on 2024-05-13 20:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admissions', '0006_alter_comments_time_alter_livestream_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isAdviser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='isCandidate',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comments',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 14, 3, 16, 21, 776586)),
        ),
        migrations.AlterField(
            model_name='livestream',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 14, 3, 16, 21, 776586)),
        ),
        migrations.AlterField(
            model_name='questions',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 14, 3, 16, 21, 777591)),
        ),
    ]
