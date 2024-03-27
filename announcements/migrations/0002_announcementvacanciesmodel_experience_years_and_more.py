# Generated by Django 4.2.7 on 2024-03-17 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcementvacanciesmodel',
            name='experience_years',
            field=models.CharField(blank=True, max_length=200, verbose_name='Количество лет опыта'),
        ),
        migrations.AddField(
            model_name='announcementvacanciesmodel',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/announcement/vacancies', verbose_name='Файл'),
        ),
        migrations.AddField(
            model_name='announcementvacanciesmodel',
            name='salary',
            field=models.CharField(blank=True, max_length=200, verbose_name='Зарплата'),
        ),
        migrations.AlterField(
            model_name='announcementfilesmodel',
            name='file',
            field=models.FileField(upload_to='uploads/announcement/documents', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='announcementfilesmodel',
            name='file_en',
            field=models.FileField(null=True, upload_to='uploads/announcement/documents', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='announcementfilesmodel',
            name='file_kk',
            field=models.FileField(null=True, upload_to='uploads/announcement/documents', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='announcementfilesmodel',
            name='file_ru',
            field=models.FileField(null=True, upload_to='uploads/announcement/documents', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='announcementimagesmodel',
            name='file',
            field=models.ImageField(upload_to='uploads/announcement/images', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='announcementimagesmodel',
            name='file_en',
            field=models.ImageField(null=True, upload_to='uploads/announcement/images', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='announcementimagesmodel',
            name='file_kk',
            field=models.ImageField(null=True, upload_to='uploads/announcement/images', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='announcementimagesmodel',
            name='file_ru',
            field=models.ImageField(null=True, upload_to='uploads/announcement/images', verbose_name='Изображение'),
        ),
    ]