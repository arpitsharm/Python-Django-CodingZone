# Generated by Django 4.2.10 on 2024-03-15 12:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="timesaStamp",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
