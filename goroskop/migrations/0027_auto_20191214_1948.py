# Generated by Django 2.2.7 on 2019-12-14 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goroskop', '0026_auto_20191214_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/'),
        ),
    ]
