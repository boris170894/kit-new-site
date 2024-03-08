# Generated by Django 4.2.7 on 2024-03-08 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('educational_work', '0002_dormitorycontactsemailmodel_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dormitorymodel',
            name='contact_email',
        ),
        migrations.RemoveField(
            model_name='dormitorymodel',
            name='contact_phone',
        ),
        migrations.RemoveField(
            model_name='dormitorymodel',
            name='documents',
        ),
        migrations.RemoveField(
            model_name='dormitorymodel',
            name='images',
        ),
        migrations.DeleteModel(
            name='DormitoryContactsEmailModel',
        ),
        migrations.DeleteModel(
            name='DormitoryContactsPhoneModel',
        ),
        migrations.DeleteModel(
            name='DormitoryFilesModel',
        ),
        migrations.DeleteModel(
            name='DormitoryImagesModel',
        ),
        migrations.DeleteModel(
            name='DormitoryModel',
        ),
    ]