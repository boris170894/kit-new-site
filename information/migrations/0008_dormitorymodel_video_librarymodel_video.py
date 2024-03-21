# Generated by Django 4.2.7 on 2024-03-18 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0007_delete_collegecontactmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='dormitorymodel',
            name='video',
            field=models.FileField(blank=True, upload_to='uploads/educational-work/dormitory/videos', verbose_name='Видео'),
        ),
        migrations.AddField(
            model_name='librarymodel',
            name='video',
            field=models.FileField(blank=True, upload_to='uploads/information/library/videos', verbose_name='Видео'),
        ),
    ]
