# Generated by Django 2.2.7 on 2019-12-14 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goroskop', '0022_userprofile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/'),
        ),
    ]