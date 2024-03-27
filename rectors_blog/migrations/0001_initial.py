# Generated by Django 4.2.7 on 2024-03-16 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RectorsBlogMainInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(blank=True, max_length=400, verbose_name='ФИО')),
                ('fio_kk', models.CharField(blank=True, max_length=400, null=True, verbose_name='ФИО')),
                ('fio_ru', models.CharField(blank=True, max_length=400, null=True, verbose_name='ФИО')),
                ('fio_en', models.CharField(blank=True, max_length=400, null=True, verbose_name='ФИО')),
                ('info', models.TextField(blank=True, verbose_name='Информация')),
                ('info_kk', models.TextField(blank=True, null=True, verbose_name='Информация')),
                ('info_ru', models.TextField(blank=True, null=True, verbose_name='Информация')),
                ('info_en', models.TextField(blank=True, null=True, verbose_name='Информация')),
                ('file', models.ImageField(blank=True, upload_to='uploads/rectors-blog/info', verbose_name='Документ')),
                ('appointment_schedule', models.CharField(blank=True, max_length=300, verbose_name='График приема')),
                ('appointment_schedule_kk', models.CharField(blank=True, max_length=300, null=True, verbose_name='График приема')),
                ('appointment_schedule_ru', models.CharField(blank=True, max_length=300, null=True, verbose_name='График приема')),
                ('appointment_schedule_en', models.CharField(blank=True, max_length=300, null=True, verbose_name='График приема')),
                ('is_public', models.BooleanField(default=False, verbose_name='Опубликовать')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Блог Ректора Главная информация',
                'verbose_name_plural': 'Блог Ректора Главная информация',
            },
        ),
        migrations.CreateModel(
            name='RectorsBlogQuestionAnswerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, max_length=100, verbose_name='Имя')),
                ('lastName', models.CharField(blank=True, max_length=100, verbose_name='Фамилия')),
                ('email', models.EmailField(blank=True, max_length=150, verbose_name='Email')),
                ('question', models.TextField(blank=True, max_length=600, verbose_name='Вопрос')),
                ('answer', models.TextField(blank=True, max_length=600, verbose_name='Ответ')),
                ('is_public', models.BooleanField(default=True, verbose_name='Опубликовать')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Блог Ректора Вопрос - Ответ',
                'verbose_name_plural': 'Блог Ректора Вопрос - Ответ',
            },
        ),
    ]