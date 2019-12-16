# Generated by Django 2.2.7 on 2019-12-12 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goroskop', '0009_auto_20191212_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=11)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='age',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='goroskop.Age'),
        ),
    ]
