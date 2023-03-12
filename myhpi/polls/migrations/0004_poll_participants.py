# Generated by Django 3.1.8 on 2021-06-12 11:28

import modelcluster.fields
from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("polls", "0003_auto_20210612_1231"),
    ]

    operations = [
        migrations.AddField(
            model_name="poll",
            name="participants",
            field=modelcluster.fields.ParentalManyToManyField(
                related_name="polls", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
