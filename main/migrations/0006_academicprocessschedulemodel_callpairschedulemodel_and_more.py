# Generated by Django 4.2.2 on 2023-09-22 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_statesymbolsmodel_desc_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicProcessScheduleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='uploads/schedule', verbose_name='График Учебного процесса')),
            ],
            options={
                'verbose_name': 'График Учебного процесса',
                'verbose_name_plural': 'График Учебного процесса',
            },
        ),
        migrations.CreateModel(
            name='CallPairScheduleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('call_schedule', models.ImageField(blank=True, upload_to='uploads/schedule', verbose_name='Расписание звонков')),
                ('pair_schedule', models.FileField(blank=True, upload_to='uploads/schedule', verbose_name='Расписание пар')),
            ],
            options={
                'verbose_name': 'Расписание звонков и расписание пар',
                'verbose_name_plural': 'Расписание звонков и расписание пар',
            },
        ),
        migrations.CreateModel(
            name='StudentEventModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Наименование')),
                ('description', models.TimeField(blank=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='Изображение')),
                ('start_date', models.DateTimeField(blank=True, verbose_name='Дата начала')),
                ('end_date', models.DateTimeField(blank=True, verbose_name='Дата конца')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'События для студента',
                'verbose_name_plural': 'События для студента',
            },
        ),
    ]
