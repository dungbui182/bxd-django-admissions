# Generated by Django 5.0.1 on 2024-05-13 20:15

import ckeditor.fields
import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admissions', '0004_universityinfo_alter_comments_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('website', models.CharField(blank=True, max_length=30)),
                ('video', models.FileField(blank=True, null=True, upload_to='')),
                ('introduction', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('program', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(default=None, upload_to='faculty/%Y/%m')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AlterField(
            model_name='comments',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 14, 3, 15, 21, 727653)),
        ),
        migrations.AlterField(
            model_name='livestream',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 14, 3, 15, 21, 743445)),
        ),
        migrations.AlterField(
            model_name='questions',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 14, 3, 15, 21, 743445)),
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('code', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=70)),
                ('faculty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='majors', to='Admissions.faculty')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
