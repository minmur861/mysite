# Generated by Django 2.2.7 on 2019-12-10 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goroskop', '0002_auto_20191210_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(default='', verbose_name='URL'),
        ),
    ]
