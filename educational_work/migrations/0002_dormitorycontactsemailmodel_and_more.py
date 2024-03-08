# Generated by Django 5.0.1 on 2024-02-10 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educational_work', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DormitoryContactsEmailModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Email общежития',
                'verbose_name_plural': 'Email общежития',
            },
        ),
        migrations.CreateModel(
            name='DormitoryContactsPhoneModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер телефона')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Телефон общежития',
                'verbose_name_plural': 'Телефон общежития',
            },
        ),
        migrations.AlterField(
            model_name='dormitorymodel',
            name='about',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='dormitorymodel',
            name='about_en',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='dormitorymodel',
            name='about_kk',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='dormitorymodel',
            name='about_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='dormitorymodel',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='dormitorymodel',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='dormitorymodel',
            name='contact_email',
            field=models.ManyToManyField(blank=True, default=[], to='educational_work.dormitorycontactsemailmodel', verbose_name='Почты'),
        ),
        migrations.AddField(
            model_name='dormitorymodel',
            name='contact_phone',
            field=models.ManyToManyField(blank=True, default=[], to='educational_work.dormitorycontactsphonemodel', verbose_name='Телефоны'),
        ),
    ]
