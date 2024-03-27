# Generated by Django 4.2.7 on 2024-03-18 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0003_announcementmodel_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcementmodel',
            name='video_en',
            field=models.FileField(blank=True, null=True, upload_to='uploads/announcement/videos', verbose_name='Видео'),
        ),
        migrations.AddField(
            model_name='announcementmodel',
            name='video_kk',
            field=models.FileField(blank=True, null=True, upload_to='uploads/announcement/videos', verbose_name='Видео'),
        ),
        migrations.AddField(
            model_name='announcementmodel',
            name='video_ru',
            field=models.FileField(blank=True, null=True, upload_to='uploads/announcement/videos', verbose_name='Видео'),
        ),
    ]