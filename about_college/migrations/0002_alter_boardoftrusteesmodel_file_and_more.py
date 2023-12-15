# Generated by Django 4.2.7 on 2023-12-15 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_college', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardoftrusteesmodel',
            name='file',
            field=models.FileField(upload_to='uploads/about_college/board_of_trustees', verbose_name='Документ'),
        ),
        migrations.AlterField(
            model_name='collegedocsmodel',
            name='college_reg',
            field=models.FileField(upload_to='uploads/about_college/docs', verbose_name='Устав'),
        ),
        migrations.AlterField(
            model_name='industrialcouncilmodel',
            name='file',
            field=models.FileField(upload_to='uploads/about_college/industrial_council', verbose_name='Документ'),
        ),
        migrations.AlterField(
            model_name='pedagogicalcouncilmodel',
            name='file',
            field=models.FileField(upload_to='uploads/about_college/pedagogical_council', verbose_name='Документ'),
        ),
    ]
