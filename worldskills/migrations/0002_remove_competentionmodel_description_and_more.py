# Generated by Django 4.2.7 on 2023-12-06 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worldskills', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competentionmodel',
            name='description',
        ),
        migrations.RemoveField(
            model_name='competentionmodel',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='competentionmodel',
            name='description_kk',
        ),
        migrations.RemoveField(
            model_name='competentionmodel',
            name='description_ru',
        ),
    ]
