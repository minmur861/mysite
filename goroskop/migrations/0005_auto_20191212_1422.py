# Generated by Django 2.2.7 on 2019-12-12 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goroskop', '0004_auto_20191210_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='URL'),
        ),
    ]