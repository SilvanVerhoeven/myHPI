# Generated by Django 3.1.8 on 2021-06-12 09:51

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0060_fix_workflow_unique_constraint"),
    ]

    operations = [
        migrations.CreateModel(
            name="Poll",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="PollChoice",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("sort_order", models.IntegerField(blank=True, editable=False, null=True)),
                ("text", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True, default="")),
                ("votes", models.IntegerField(default=0)),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="choices",
                        to="polls.poll",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
    ]
