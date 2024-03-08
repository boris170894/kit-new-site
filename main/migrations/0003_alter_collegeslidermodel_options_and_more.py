# Generated by Django 5.0.1 on 2024-02-09 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_collegeslidermodel_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collegeslidermodel',
            options={'verbose_name': 'Cлайдер на главной странице', 'verbose_name_plural': 'Cлайдер на главной странице'},
        ),
        migrations.AlterField(
            model_name='collegesliderimagemodel',
            name='status_1',
            field=models.BooleanField(default=False, verbose_name='Отметить как главное изображение'),
        ),
        migrations.AlterField(
            model_name='collegesliderimagemodel',
            name='status_2',
            field=models.BooleanField(default=False, verbose_name='Отметить как второе изображение'),
        ),
        migrations.AlterField(
            model_name='collegesliderimagemodel',
            name='status_3',
            field=models.BooleanField(default=False, verbose_name='Отметить как третье изображение'),
        ),
    ]