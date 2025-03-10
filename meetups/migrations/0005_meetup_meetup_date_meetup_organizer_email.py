# Generated by Django 5.1.6 on 2025-03-06 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meetups", "0004_participant_meetup_participants"),
    ]

    operations = [
        migrations.AddField(
            model_name="meetup",
            name="meetup_date",
            field=models.DateField(default="2025-03-03"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="meetup",
            name="organizer_email",
            field=models.EmailField(default="test@test.com", max_length=254),
            preserve_default=False,
        ),
    ]
