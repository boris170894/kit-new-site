# Generated by Django 4.2.7 on 2023-12-14 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('educational_work', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='generalinformationfilesmodel',
            options={'verbose_name': 'Файлы для страницы общей информации', 'verbose_name_plural': 'Файлы для страницы  общей информации'},
        ),
        migrations.DeleteModel(
            name='GeneralInformationModel',
        ),
    ]