# Generated by Django 5.1.6 on 2025-03-03 00:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("room_types", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_archived", models.BooleanField(default=False)),
                ("name", models.CharField(max_length=50)),
                (
                    "room_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="room_types.roomtype",
                    ),
                ),
            ],
        ),
    ]
