# Generated by Django 2.2.7 on 2019-12-16 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goroskop', '0029_auto_20191216_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/'),
        ),
        migrations.DeleteModel(
            name='Avatar',
        ),
    ]
