# Generated by Django 2.1 on 2018-09-12 12:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_event_attendees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(related_name='event_attendees', through='event.Attendee', to=settings.AUTH_USER_MODEL),
        ),
    ]
