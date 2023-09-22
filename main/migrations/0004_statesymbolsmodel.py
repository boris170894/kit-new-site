# Generated by Django 4.2.2 on 2023-09-20 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_collegedocsmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='StateSymbolsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Название')),
                ('name_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('name_kk', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('image', models.ImageField(blank=True, upload_to='upload/state-symbols', verbose_name='Изображение')),
                ('desc', models.TextField(verbose_name='Описание')),
                ('desc_ru', models.TextField(null=True, verbose_name='Описание')),
                ('desc_kk', models.TextField(null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Государственные Символы',
                'verbose_name_plural': 'Государственные Символы',
            },
        ),
    ]