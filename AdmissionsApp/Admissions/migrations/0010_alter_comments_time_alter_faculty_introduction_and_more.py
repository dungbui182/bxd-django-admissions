# Generated by Django 5.0.1 on 2024-05-15 15:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admissions', '0009_alter_comments_time_alter_livestream_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 15, 22, 24, 2, 858829)),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='introduction',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='program',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='livestream',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 15, 22, 24, 2, 858829)),
        ),
        migrations.AlterField(
            model_name='questions',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 15, 22, 24, 2, 858829)),
        ),
        migrations.AlterField(
            model_name='universityinfo',
            name='introduction',
            field=models.TextField(blank=True, null=True),
        ),
    ]
