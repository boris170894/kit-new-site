# Generated by Django 4.2.7 on 2024-03-16 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnnouncementFilesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название файла')),
                ('title_kk', models.CharField(max_length=255, null=True, verbose_name='Название файла')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Название файла')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='Название файла')),
                ('file', models.FileField(upload_to='uploads/information/our-union/documents', verbose_name='Файл')),
                ('file_kk', models.FileField(null=True, upload_to='uploads/information/our-union/documents', verbose_name='Файл')),
                ('file_ru', models.FileField(null=True, upload_to='uploads/information/our-union/documents', verbose_name='Файл')),
                ('file_en', models.FileField(null=True, upload_to='uploads/information/our-union/documents', verbose_name='Файл')),
                ('is_public', models.BooleanField(default=True, verbose_name='Опубликовать')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Объявления, Файлы',
                'verbose_name_plural': 'Объявления, Файлы',
            },
        ),
        migrations.CreateModel(
            name='AnnouncementImagesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='uploads/information/our-union/images', verbose_name='Изображение')),
                ('file_kk', models.ImageField(null=True, upload_to='uploads/information/our-union/images', verbose_name='Изображение')),
                ('file_ru', models.ImageField(null=True, upload_to='uploads/information/our-union/images', verbose_name='Изображение')),
                ('file_en', models.ImageField(null=True, upload_to='uploads/information/our-union/images', verbose_name='Изображение')),
                ('is_public', models.BooleanField(default=True, verbose_name='Опубликовать')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Объявления, Фото',
                'verbose_name_plural': 'Объявления, Фото',
            },
        ),
        migrations.CreateModel(
            name='AnnouncementModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('about_kk', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('about_ru', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('about_en', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('is_public', models.BooleanField(default=False, verbose_name='Опубликовать')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Объявления',
                'verbose_name_plural': 'Объявления',
            },
        ),
        migrations.CreateModel(
            name='AnnouncementVacanciesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('title_kk', models.CharField(max_length=200, null=True, verbose_name='Название')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='Название')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('description_kk', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('is_public', models.BooleanField(default=False, verbose_name='Опубликовать')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Объявления, вакансии',
                'verbose_name_plural': 'Объявления, вакансии',
            },
        ),
    ]
