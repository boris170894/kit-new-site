# Generated by Django 4.2.7 on 2024-03-08 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_college', '0004_collegetexthistorymodel_our_mission'),
    ]

    operations = [
        migrations.AddField(
            model_name='collegetexthistorymodel',
            name='our_mission_en',
            field=models.TextField(blank=True, null=True, verbose_name='Наша миссия'),
        ),
        migrations.AddField(
            model_name='collegetexthistorymodel',
            name='our_mission_kk',
            field=models.TextField(blank=True, null=True, verbose_name='Наша миссия'),
        ),
        migrations.AddField(
            model_name='collegetexthistorymodel',
            name='our_mission_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Наша миссия'),
        ),
    ]