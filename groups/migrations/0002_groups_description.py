# Generated by Django 4.1.1 on 2023-10-20 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='description',
            field=models.CharField(default='', max_length=100),
        ),
    ]
