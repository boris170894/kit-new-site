# Generated by Django 4.2.7 on 2023-12-07 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worldskills', '0003_competentiondocumentationmodel_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='competentiondocumentationmodel',
            name='title_en',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='competentiondocumentationmodel',
            name='title_kk',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='competentiondocumentationmodel',
            name='title_ru',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]