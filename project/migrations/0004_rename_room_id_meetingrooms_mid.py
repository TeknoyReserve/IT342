# Generated by Django 4.0.2 on 2022-03-21 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_meetingrooms_meeting_room'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meetingrooms',
            old_name='room_id',
            new_name='mid',
        ),
    ]
