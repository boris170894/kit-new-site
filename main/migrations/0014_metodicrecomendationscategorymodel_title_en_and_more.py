# Generated by Django 4.2.7 on 2023-12-04 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_metodicrecomendationscategorymodel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='metodicrecomendationscategorymodel',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Наименования'),
        ),
        migrations.AddField(
            model_name='metodicrecomendationscategorymodel',
            name='title_kk',
            field=models.CharField(max_length=200, null=True, verbose_name='Наименования'),
        ),
        migrations.AddField(
            model_name='metodicrecomendationscategorymodel',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Наименования'),
        ),
        migrations.AddField(
            model_name='metodicrecomendationsdocumentmodel',
            name='title_en',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Наименование'),
        ),
        migrations.AddField(
            model_name='metodicrecomendationsdocumentmodel',
            name='title_kk',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Наименование'),
        ),
        migrations.AddField(
            model_name='metodicrecomendationsdocumentmodel',
            name='title_ru',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Наименование'),
        ),
    ]
