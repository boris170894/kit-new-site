# Generated by Django 4.2.2 on 2023-06-30 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollegePartnersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('partner_name_ru', models.CharField(max_length=200, null=True, verbose_name='Наименование')),
                ('partner_name_kk', models.CharField(max_length=200, null=True, verbose_name='Наименование')),
                ('partner_logo', models.ImageField(blank=True, upload_to='upload/partners', verbose_name='Лого')),
                ('partner_url', models.CharField(blank=True, max_length=100, verbose_name='Ссылка на сайт')),
            ],
            options={
                'verbose_name': 'Партнёры колледжа',
                'verbose_name_plural': 'Партнёры колледжа',
            },
        ),
        migrations.AlterModelOptions(
            name='collegecontactmodel',
            options={'verbose_name': 'Контакты', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.AddField(
            model_name='collegecontactmodel',
            name='addr_kk',
            field=models.CharField(max_length=300, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='collegecontactmodel',
            name='addr_ru',
            field=models.CharField(max_length=300, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='collegecontactmodel',
            name='priem_com',
            field=models.CharField(default='', max_length=20, verbose_name='Приёмная комиссия'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collegecontactmodel',
            name='wats',
            field=models.CharField(default='', max_length=20, verbose_name='Watsapp'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collegehistorymodel',
            name='info_kk',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='collegehistorymodel',
            name='info_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
    ]
