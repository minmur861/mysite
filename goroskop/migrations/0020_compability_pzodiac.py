# Generated by Django 2.2.7 on 2019-12-14 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goroskop', '0019_auto_20191213_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='compability',
            name='pzodiac',
            field=models.CharField(default='Gemini', max_length=40),
        ),
    ]
