# Generated by Django 5.1.6 on 2025-03-06 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meetups", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="meetup",
            name="image",
            field=models.ImageField(default="test", upload_to="images"),
            preserve_default=False,
        ),
    ]
