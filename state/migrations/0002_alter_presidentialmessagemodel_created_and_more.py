# Generated by Django 5.0.1 on 2024-02-21 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('state', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presidentialmessagemodel',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='presidentialmessagemodel',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
