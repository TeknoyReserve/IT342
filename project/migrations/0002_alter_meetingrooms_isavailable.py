# Generated by Django 4.0.2 on 2022-04-05 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingrooms',
            name='isAvailable',
            field=models.BooleanField(default=True),
        ),
    ]
