# Generated by Django 3.0.7 on 2020-07-16 09:15

import annoying.fields
from django.conf import settings
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("api", "0036_auto_20200716_1021"),
    ]

    operations = [
        migrations.AlterField(
            model_name="elo",
            name="player",
            field=annoying.fields.AutoOneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="elo",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
