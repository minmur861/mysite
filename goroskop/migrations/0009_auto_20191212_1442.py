# Generated by Django 2.2.7 on 2019-12-12 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goroskop', '0008_auto_20191212_1437'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={},
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='slug',
        ),
    ]
