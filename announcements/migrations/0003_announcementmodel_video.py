# Generated by Django 4.2.7 on 2024-03-18 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0002_announcementvacanciesmodel_experience_years_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcementmodel',
            name='video',
            field=models.FileField(blank=True, upload_to='uploads/announcement/videos', verbose_name='Видео'),
        ),
    ]