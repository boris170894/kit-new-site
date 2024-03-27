# Generated by Django 4.2.7 on 2024-03-18 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0008_dormitorymodel_video_librarymodel_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='dormitorymodel',
            name='video_en',
            field=models.FileField(blank=True, null=True, upload_to='uploads/educational-work/dormitory/videos', verbose_name='Видео'),
        ),
        migrations.AddField(
            model_name='dormitorymodel',
            name='video_kk',
            field=models.FileField(blank=True, null=True, upload_to='uploads/educational-work/dormitory/videos', verbose_name='Видео'),
        ),
        migrations.AddField(
            model_name='dormitorymodel',
            name='video_ru',
            field=models.FileField(blank=True, null=True, upload_to='uploads/educational-work/dormitory/videos', verbose_name='Видео'),
        ),
        migrations.AddField(
            model_name='librarymodel',
            name='video_en',
            field=models.FileField(blank=True, null=True, upload_to='uploads/information/library/videos', verbose_name='Видео'),
        ),
        migrations.AddField(
            model_name='librarymodel',
            name='video_kk',
            field=models.FileField(blank=True, null=True, upload_to='uploads/information/library/videos', verbose_name='Видео'),
        ),
        migrations.AddField(
            model_name='librarymodel',
            name='video_ru',
            field=models.FileField(blank=True, null=True, upload_to='uploads/information/library/videos', verbose_name='Видео'),
        ),
        migrations.AddField(
            model_name='ourunionmodel',
            name='video',
            field=models.FileField(blank=True, upload_to='uploads/educational-work/dormitory/videos', verbose_name='Видео'),
        ),
        migrations.AddField(
            model_name='ourunionmodel',
            name='video_en',
            field=models.FileField(blank=True, null=True, upload_to='uploads/educational-work/dormitory/videos', verbose_name='Видео'),
        ),
        migrations.AddField(
            model_name='ourunionmodel',
            name='video_kk',
            field=models.FileField(blank=True, null=True, upload_to='uploads/educational-work/dormitory/videos', verbose_name='Видео'),
        ),
        migrations.AddField(
            model_name='ourunionmodel',
            name='video_ru',
            field=models.FileField(blank=True, null=True, upload_to='uploads/educational-work/dormitory/videos', verbose_name='Видео'),
        ),
    ]