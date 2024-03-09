# Generated by Django 4.2.7 on 2024-03-08 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0003_dormitorycontactsemailmodel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurUnionFilesModel',
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
                'verbose_name': 'Наш профсоюз Файлы',
                'verbose_name_plural': 'Наш профсоюз Файлы',
            },
        ),
        migrations.CreateModel(
            name='OurUnionImagesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='uploads/information/our-union/images', verbose_name='Изображение')),
                ('is_public', models.BooleanField(default=True, verbose_name='Опубликовать')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Наш профсоюз Фото',
                'verbose_name_plural': 'Наш профсоюз Фото',
            },
        ),
        migrations.CreateModel(
            name='OurUnionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('about_kk', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('about_ru', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('about_en', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('documents', models.ManyToManyField(blank=True, default=[], related_name='Файлы', to='information.ourunionfilesmodel')),
                ('images', models.ManyToManyField(blank=True, default=[], related_name='Изображения', to='information.ourunionimagesmodel')),
            ],
            options={
                'verbose_name': 'Наш профсоюз',
                'verbose_name_plural': 'Наш профсоюз',
            },
        ),
    ]